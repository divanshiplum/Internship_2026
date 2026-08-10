# 🎓 Internship Tasks & Projects

Welcome to my **Internship Project Repository**! This repository hosts a curated collection of Python scripts, Streamlit web applications, and educational playbooks developed during my internship days. It progresses from core Python scripting concepts to fully-fledged interactive Streamlit dashboards and utility applications.

---

## 📁 Repository Structure

Here is a breakdown of the daily tasks, demonstrations, and learning materials:

```bash
├── Day2/
│   ├── Day2_Python_Properly_HinduCollegeAmritsar_Zlaark.pptx  # Python concepts guide
│   └── extract-year.py                                         # Python script to parse dates
├── Day3/
│   └── Git_GitHub.pptx                                         # Git and GitHub basics playbook
├── Day4/
│   ├── Meet_Streamlit.pptx                                     # Streamlit fundamentals playbook
│   └── unit-converter.py                                       # Interactive streamlit unit converter
├── Day5/
│   ├── Widgets_Layout.pptx                                     # Layouts & widgets guide
│   ├── column-demo.py                                          # Multi-column layout demo
│   ├── container-demo.py                                       # st.container demo
│   ├── counter-broken.py                                       # State management issue demo
│   ├── counter-fixed.py                                        # State management solution (st.session_state)
│   ├── empty-demo.py                                           # Dynamic content placeholders (st.empty)
│   ├── expander-demo.py                                        # Collapsible content layouts (st.expander)
│   ├── keys-demo.py                                            # Advanced widget key referencing demo
│   ├── sidebar-demo.py                                         # Multi-widget sidebar control panel demo
│   └── tabs-demo.py                                            # tab-based navigation layout demo
├── feedback-form.py                                            # Complete interactive user feedback app
├── Project Playbook.pptx                                       # Overall project outline
└── README.md                                                   # Project documentation
```

---

## 🛠️ Detailed App Features

### 1. 📝 Feedback Form (`feedback-form.py`)
A comprehensive feedback form built with Streamlit widgets inside a structured container.
* **Fields:** Name, Email, Gender (dropdown selection), Experience Rating (decimal slider), Feedback comment text area, and Suggestions.
* **Features:** Built-in form validation (ensures fields are filled before submitting) and an interactive results display showing submitted feedback in real-time.

### 2. 🔢 Unit Converter (`Day4/unit-converter.py`)
A multi-category measurement converter.
* **Supported Conversions:** Length (Metres to Feet), Weight (Kilograms to Pounds), and Temperature (Celsius to Fahrenheit).
* **UI:** Dynamic widget adjustments depending on selected conversion type.

---

## 💻 How to Run Locally

Follow these steps to set up and run any of the applications on your system:

### 1. Clone the Repository
```bash
git clone https://github.com/divanshiplum/Internship_2026.git
cd Internship_2026
```

### 2. Set Up a Virtual Environment (Recommended)
Using a virtual environment keeps your global Python installation clean:
```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it
# On Mac/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies
Install the required package (Streamlit):
```bash
pip install streamlit
```

### 4. Run the Apps
You can run any of the Streamlit apps using `streamlit run`:
```bash
# Run the main feedback form:
streamlit run feedback-form.py

# Run the unit converter:
streamlit run Day4/unit-converter.py

# Run any layout demo (e.g., sidebar demo):
streamlit run Day5/sidebar-demo.py
```

---

## ☁️ Deploying to Streamlit Cloud

To host these applications live on the web for free:
1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/) with your GitHub account.
2. Click **Create app**.
3. Choose this repository (`Internship_2026`).
4. Set the **Main file path** to `feedback-form.py` (or `Day4/unit-converter.py`).
5. Click **Deploy!**
