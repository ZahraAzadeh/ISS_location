# ISS Tracker 🚀

A simple Python program that uses the **Open Notify API** to:

- Get the current location of the International Space Station (ISS)
- Show the astronauts currently in space
- Display a simple text-based menu for navigation

---

## 📌 Features

### 1️⃣ Show ISS Current Location
- Fetches live latitude and longitude
- Generates an OpenStreetMap link so you can view the ISS on a map

### 2️⃣ Show Astronauts in Space
- Fetches how many astronauts are currently in orbit
- Displays their names and spacecraft

### 3️⃣ Simple Interactive Menu
A command-line menu lets you choose:

Show current location of the ISS

Show astronauts currently in space

Exit

yaml
Copy code

---

## 🔧 Installation

### Clone the repository:
```sh
git clone https://github.com/YOUR_USERNAME/your_repo_name.git
cd your_repo_name
Install dependencies:
sh
Copy code
pip install -r requirements.txt
▶️ How to Run
sh
Copy code
python main.py
📡 APIs Used
This project uses the free Open Notify API:

ISS Location:
http://api.open-notify.org/iss-now.json

Astronauts in Space:
http://api.open-notify.org/astros.json

No API keys are required.

⚙️ GitHub Actions Workflow
This repository includes a GitHub Actions workflow located at:

arduino
Copy code
.github/workflows/run.yml
It allows you to run the script manually from the Actions tab:

Sets up Python 3.10

Installs dependencies

Runs the script

📁 Project Structure
arduino
Copy code
.
├── main.py
├── README.md
├── requirements.txt
└── .github
    └── workflows
        └── run.yml
