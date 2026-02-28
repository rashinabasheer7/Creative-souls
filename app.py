from flask import (
    Flask, request, jsonify, render_template,
    redirect, url_for, session
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import os
from functools import wraps

app = Flask(__name__)
CORS(app, supports_credentials=True)

# ── Configuration ──────────────────────────────────────
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventhub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False          # ← must be False for HTTP localhost
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=24)

db = SQLAlchemy(app)

# ── Models ─────────────────────────────────────────────

class User(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(150), unique=True, nullable=False)
    student_id = db.Column(db.String(50), unique=True, nullable=False)
    password   = db.Column(db.String(255), nullable=False)
    role       = db.Column(db.String(20), default='student')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            'id':         self.id,
            'name':       self.name,
            'email':      self.email,
            'student_id': self.student_id,
            'role':       self.role,
        }

class Event(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(100), nullable=False)
    poster = db.Column(db.Text, nullable=False)

class Registration(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_id   = db.Column(db.String(50), nullable=False)
    event_name   = db.Column(db.String(100), nullable=False)
    role         = db.Column(db.String(20), nullable=False)

with app.app_context():
    db.create_all()

# ── Auth decorators ────────────────────────────────────

def login_required(f):
    """Redirect to /login if no active session."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated

def api_login_required(f):
    """Return 401 JSON if no active session (for API routes)."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    """Return 403 JSON if user is not admin (for API routes)."""
    @wraps(f)
    @api_login_required
    def decorated(*args, **kwargs):
        if session.get('role') != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        return f(*args, **kwargs)
    return decorated

# ── Page routes ────────────────────────────────────────

@app.route('/')
@login_required          # ← server-side guard: no session = redirect to /login
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    # Already logged in → skip to app
    if 'user_id' in session:
        return redirect(url_for('index'))
    return render_template('login.html')

# ── Auth API ───────────────────────────────────────────

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    name       = (data.get('name') or '').strip()
    email      = (data.get('email') or '').strip().lower()
    student_id = (data.get('student_id') or '').strip()
    password   = data.get('password', '')
    role       = data.get('role', 'student')

    if not name or len(name) < 2:
        return jsonify({'error': 'Name must be at least 2 characters'}), 422
    if not email or '@' not in email:
        return jsonify({'error': 'Enter a valid email address'}), 422
    if not student_id:
        return jsonify({'error': 'Student ID is required'}), 422
    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters'}), 422
    if role not in ('student', 'admin'):
        return jsonify({'error': 'Invalid role'}), 422

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'An account with this email already exists'}), 409
    if User.query.filter_by(student_id=student_id).first():
        return jsonify({'error': 'This Student ID is already registered'}), 409

    user = User(
        name=name, email=email, student_id=student_id,
        password=generate_password_hash(password), role=role
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Account created successfully', 'user': user.to_dict()}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    email    = (data.get('email') or '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 422

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Store user info in server-side session (signed cookie)
    session.permanent = True
    session['user_id'] = user.id
    session['role']    = user.role
    session['name']    = user.name

    return jsonify({'message': 'Login successful', 'user': user.to_dict()}), 200

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'}), 200

@app.route('/api/auth/me', methods=['GET'])
@api_login_required
def get_current_user():
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# ── Events API ─────────────────────────────────────────

@app.route('/api/events', methods=['GET'])
@api_login_required
def get_events():
    events = Event.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'poster': e.poster} for e in events])

@app.route('/api/events', methods=['POST'])
@admin_required
def create_event():
    data = request.get_json(silent=True)
    if not data or not data.get('name') or not data.get('poster'):
        return jsonify({'error': 'name and poster are required'}), 400
    event = Event(name=data['name'].strip(), poster=data['poster'])
    db.session.add(event)
    db.session.commit()
    return jsonify({'message': 'Event created!', 'id': event.id}), 201

@app.route('/api/events/<int:id>', methods=['DELETE'])
@admin_required
def delete_event(id):
    event = Event.query.get(id)
    if not event:
        return jsonify({'error': 'Event not found'}), 404
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200

# ── Registrations API ──────────────────────────────────

@app.route('/api/register', methods=['GET'])
@api_login_required
def get_registrations():
    regs = Registration.query.all()
    return jsonify([{
        'id': r.id, 'name': r.student_name,
        'student_id': r.student_id, 'event': r.event_name, 'role': r.role
    } for r in regs])

@app.route('/api/register', methods=['POST'])
@api_login_required
def create_registration():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    name  = (data.get('name') or '').strip()
    sid   = (data.get('id') or '').strip()
    event = (data.get('event') or '').strip()
    role  = data.get('role', 'Participant')

    if not name or not sid or not event:
        return jsonify({'error': 'name, id, and event are required'}), 422
    if role not in ('Participant', 'Volunteer'):
        return jsonify({'error': 'Invalid role'}), 422

    existing = Registration.query.filter_by(student_id=sid, event_name=event).first()
    if existing:
        return jsonify({'error': 'Already registered for this event'}), 409

    reg = Registration(student_name=name, student_id=sid, event_name=event, role=role)
    db.session.add(reg)
    db.session.commit()
    return jsonify({'message': 'Registered!', 'id': reg.id}), 201

@app.route('/api/register/<int:id>', methods=['DELETE'])
@admin_required
def delete_registration(id):
    reg = Registration.query.get(id)
    if not reg:
        return jsonify({'error': 'Registration not found'}), 404
    db.session.delete(reg)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200

# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
