<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [EventHub] 🎯

## Basic Details

### Team Name: [Creative Souls]

### Team Members
- Member 1: [Rashinamol B] - [Ahalia School of Engineering & Technology]
- Member 2: [Roshna Fathima.Y] - [Ahalia School of Engineering & Technology]

### Hosted Project Link
[mention your project hosted link here]

### Project Description
The College EventHub Portal is a web application designed to bridge the communication gap between student organizations and the campus community. It serves as a centralized digital bulletin board where students can discover upcoming fests, workshops, and seminars in real-time. The system replaces traditional, inefficient methods like physical posters or fragmented messaging apps with a modern, responsive interface that handles everything from event discovery to student registration.

### The Problem statement
Educational institutions often struggle with fragmented communication regarding campus events, leading to low student engagement and disorganized record-keeping. Manual registration processes via paper forms or disparate spreadsheets are prone to data entry errors and make real-time event tracking nearly impossible for administrators.

### The Solution
EventHub provides a centralized, a platform that automates college event workflows by integrating secure administrator controls with a real-time student registration interface. It replaces manual paperwork with a persistent SQLite database and a seamless Flask-driven UI to ensure efficient data tracking and campus-wide event visibility.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [Python (Backend logic), JavaScript (Frontend interactivity), HTML5/CSS3 (Structure and Styling), and SQL (Database queries)]
- Frameworks used: [Flask (A lightweight WSGI web application framework for Python]
- Libraries used: [SQLite3: For server-side relational data storage.Werkzeug: Specifically for security features like generate_password_hash and check_password_hash.]
- Tools used: [VS Code (Code Editor), Google Chrome DevTools (Debugging and API testing), and Python IDLE/Terminal (Running the server).]

**For Hardware:**
- Main components: [A standard workstation or laptop acting as the Localhost server]
- Specifications: [Processor: Dual-core 2.0GHz or higher.
.RAM: Minimum 4GB (8GB recommended for smooth multitasking).
.Storage: At least 100MB of free space for the SQLite database file and project assets.]
- Tools required: [Internet Connection: Required for loading external Google Fonts and CSS libraries.
Web Browser: Any modern browser (Chrome, Firefox, or Edge) to render the UI.]

---

## Features

List the key features of your project:
- Feature 1: [Secure Admin Dashboard: A protected management area that allows authorized users to post new events with custom titles and poster images, as well as delete outdated listings.]
- Feature 2: [Real-time Event Feed: A dynamic, visually engaging home page that automatically updates to show the latest college events stored in the database.]
- Feature 3: [Integrated Student Registration: A seamless digital form where students can register for events by selecting their name, ID, and specific role (Participant or Volunteer)]
- Feature 4: [Automated Records Management: A dedicated records page that pulls data directly from the SQLite database to display all student registrations in an organized table for administrative review.]

---

## Implementation

### For Software:

#### Installation
```bash
[Inblinker==1.9.0
click==8.3.1
colorama==0.4.6
Flask==3.1.3
flask-cors==6.0.2
Flask-SQLAlchemy==3.1.1
greenlet==3.3.2
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
SQLAlchemy==2.0.47
typing_extensions==4.15.0
Werkzeug==3.1.6
stallation commands - e.g., npm install, pip install -r requirements.txt]
```

#### Run
```bash
[Run commands - e.g., npm start, python app.py]
```

### For Hardware:

#### Components Required
[List all components needed with specifications]

#### Circuit Setup
[Explain how to set up the circuit]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

<img width="1919" height="934" alt="image" src="https://github.com/user-attachments/assets/2b8876bb-f912-447b-88f9-18476e359b62" />
Secure Access Management: Empowering campus engagement through role-based authentication and a streamlined registration experience.

<img width="1842" height="902" alt="image" src="https://github.com/user-attachments/assets/5cdd5d0e-e0be-4db9-80ab-a724e85e8c3a" />
"Seamless User Journey: From Secure Role-Based Login to a Centralized Management Hub for Campus Events."


<img width="1894" height="936" alt="image" src="https://github.com/user-attachments/assets/0a4c6381-1dda-4cb5-b516-1a149fca0fe3" />
"Secure User Onboarding: Empowering the campus community with a modern, intuitive registration flow that distinguishes between Student event-discovery and Admin management roles."

<img width="1917" height="943" alt="image" src="https://github.com/user-attachments/assets/c3dad5b1-af42-4b7f-9a60-45ad198b8ac3" />
"From Authentication to Discovery: A comprehensive overview of the EventHub journey, featuring the multi-role 'Create Account' interface and the authenticated 'Upcoming Events' dashboard."

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
https://drive.google.com/file/d/1MHEsOY4DyvZPssyblWkiRoBRR-vO3bnC/view?usp=sharing

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
