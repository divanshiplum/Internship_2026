<div align="center">

  # 🎓 Internship Tasks & Projects
  
  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://internship2026-zarqnvicjwecp8wadn4cuw.streamlit.app/)
  [![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

  <p align="center">
    <b>An interactive suite of Python tasks, concepts, and web dashboards.</b>
    <br />
    Explore the daily tasks, tools, and fully-fledged Streamlit web applications developed during the internship.
  </p>

  <h3>
    <a href="https://internship2026-zarqnvicjwecp8wadn4cuw.streamlit.app/">👉 View Live Web Application 👈</a>
  </h3>

  ---
</div>

## 📷 Application Preview

<div align="center">
  <img src="https://github.com/user-attachments/assets/1ebdfd58-aaab-40a6-8ae4-5f64fc734df0" width="400" alt="App Preview" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
  <br />
</div>
---

## 📁 Repository Map

Navigate through the folders to check daily tasks and lectures:

```bash
📂 Internship_2026
├── 📁 Day2/
│   ├── 📝 Day2_Python_Properly_HinduCollegeAmritsar_Zlaark.pptx  # Concepts guide
│   └── ⚙️ extract-year.py                                         # Parse year from date string
├── 📁 Day3/
│   └── 📝 Git_GitHub.pptx                                         # Git setup & workflow playbook
├── 📁 Day4/
│   ├── 📝 Meet_Streamlit.pptx                                     # Streamlit fundamentals guide
│   └── 🔢 unit-converter.py                                       # Dynamic unit conversion app
├── 📁 Day5/
│   ├── 📝 Widgets_Layout.pptx                                     # UI layout design principles
│   ├── ⚙️ column-demo.py                                          # Multi-column grid demo
│   ├── ⚙️ container-demo.py                                       # Containerized widget layout
│   ├── ⚙️ counter-broken.py                                       # State management challenges
│   ├── ⚙️ counter-fixed.py                                        # State management using st.session_state
│   ├── ⚙️ empty-demo.py                                           # Dynamic content replacement (st.empty)
│   ├── ⚙️ expander-demo.py                                        # Collapsible interface elements
│   ├── ⚙️ keys-demo.py                                            # Differentiating inputs using keys
│   ├── ⚙️ sidebar-demo.py                                         # Collapsible sidebar control panel
│   └── ⚙️ tabs-demo.py                                            # Tabbed layout navigation demo
├── 📝 feedback-form.py                                            # Comprehensive interactive user feedback app
├── 📝 calculator.py                                               # interactive calculator application for performing basic arithmetic operations and calculations.
├── 📝 to-do-list.py                                               # task management application for adding, viewing, updating, and managing daily tasks.
├── 📝 Project Playbook.pptx                                       # Overall project scope presentation
└── 📄 README.md                                                   # Visual project index
```

---

## 🛠️ Main App Showcases

### 📝 Interactive Feedback Form (`feedback-form.py`)
A feedback portal configured to validate user input and display submissions in real time.
* **Fields:** Name, Email, Gender (dropdown), Experience Rating (star rating helper), Feedback comments, and suggestions.
* **UI Features:** Grouped container structures, form lock checks, and success/warning notification states.

### 🔢 Dynamic Unit Converter (`Day4/unit-converter.py`)
A fast-calculating unit conversion system.
* **Categories:** Length (Metres ⇄ Feet), Weight (Kilograms ⇄ Pounds), and Temperature (Celsius ⇄ Fahrenheit).
* **UI Features:** Responsive input controls that calculate results immediately as values change.

### 🧮 Calculator App (`calculator.py`)
A simple arithmetic calculator for performing basic mathematical operations.
* **Operations:** Addition, Subtraction, Multiplication, and Division.
* **UI Features:** Interactive input handling with clear operation selection and result display.

### 📝 To-Do List App (`to-do-list.py`)
A simple task management application for organizing and tracking daily tasks.
* **Task Management:** Add, view, update, and delete tasks.
* **UI Features:** Interactive task input and status management for keeping track of completed and pending tasks. 

---

## 💻 How to Run Locally

Get the application running on your local machine:

### 1. Clone & Navigate
```bash
git clone https://github.com/divanshiplum/Internship_2026.git
cd Internship_2026
```

### 2. Set Up a Virtual Environment
Keep your local machine's python environment isolated and clean:
```bash
# Create the environment
python3 -m venv .venv

# Activate it (Mac/Linux)
source .venv/bin/activate

# Activate it (Windows)
.venv\Scripts\activate
```

### 3. Install Requirements & Run
```bash
# Install Streamlit library
pip install streamlit

# Start the main feedback application
streamlit run feedback-form.py
```

---

## ☁️ Continuous Deployment to Streamlit Cloud

To host these applications live for free:
1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/) with your GitHub account.
2. Click **Create app**.
3. Choose this repository (`Internship_2026`).
4. Set the **Main file path** to `feedback-form.py`.
5. Click **Deploy!**

---

<div align="center">
  <sub>Developed during my Python & Streamlit Internship. Powered by Python 🐍 and Streamlit 🎈.</sub>
</div>
