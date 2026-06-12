# \# 🌍 EcoTrack AI – Carbon Footprint Analyzer

# 

# EcoTrack AI is a Flask-based web application that helps users calculate and understand their carbon footprint based on daily activities such as travel, electricity usage, and dietary habits. It provides impact classification and personalized eco-friendly recommendations.

# 

# \---

# 

# \## 🚀 Features

# 

# \* 🌱 Carbon footprint score calculation

# \* 📊 Impact classification (Low / Moderate / High)

# \* 💡 Personalized sustainability recommendations

# \* 🌍 Web UI for user interaction

# \* 📡 REST API for programmatic access

# \* 🧪 Fully tested backend using pytest

# \* 📈 HTML test reports + coverage reports

# 

# \---

# 

# \## 🏗️ Tech Stack

# 

# \* Python 3

# \* Flask

# \* HTML / CSS

# \* Pytest

# \* Requests

# 

# \---

# 

# \## 📡 API Documentation

# 

# \### ▶ Endpoint

# 

# ```

# POST /api/calculate

# ```

# 

# \### 📥 Request Body

# 

# ```json

# {

# &#x20; "travel": 50,

# &#x20; "electricity": 100,

# &#x20; "diet": "vegetarian"

# }

# ```

# 

# \### 📤 Response

# 

# ```json

# {

# &#x20; "score": 56.0,

# &#x20; "category": "Moderate Impact",

# &#x20; "recommendation": "Your carbon footprint is moderate. Small lifestyle changes can make a big difference.",

# &#x20; "tips": \[

# &#x20;   "Turn off unused appliances",

# &#x20;   "Reduce unnecessary travel",

# &#x20;   "Use energy-efficient devices",

# &#x20;   "Track monthly electricity usage"

# &#x20; ]

# }

# ```

# 

# \---

# 

# \## ▶️ How to Run the Project

# 

# \### 1. Clone the repository

# 

# ```bash

# git clone https://github.com/M-DeviSri/eco-track-ai.git

# cd eco-track-ai

# ```

# 

# \### 2. Create virtual environment

# 

# ```bash

# python -m venv venv

# ```

# 

# \### 3. Activate environment

# 

# \*\*Windows:\*\*

# 

# ```bash

# venv\\Scripts\\activate

# ```

# 

# \*\*Mac/Linux:\*\*

# 

# ```bash

# source venv/bin/activate

# ```

# 

# \### 4. Install dependencies

# 

# ```bash

# pip install flask pytest requests pytest-cov pytest-html

# ```

# 

# \---

# 

# \## ▶️ Run the Application

# 

# ```bash

# python app.py

# ```

# 

# Open in browser:

# 

# ```

# http://127.0.0.1:5000

# ```

# 

# \---

# 

# \## 🧪 Run Tests

# 

# \### Run all tests

# 

# ```bash

# pytest -v

# ```

# 

# \### Generate HTML test report

# 

# ```bash

# pytest -v --html=report.html --self-contained-html

# ```

# 

# \### Run coverage report

# 

# ```bash

# pytest --cov=app --cov-report=term-missing

# ```

# 

# \---

# 

# \## 📊 Project Highlights

# 

# \* ✔ Fully functional Flask API

# \* ✔ Real-time carbon footprint calculation

# \* ✔ Edge case handling

# \* ✔ Automated test suite (7/7 passing)

# \* ✔ HTML test reporting

# \* ✔ Code coverage reporting (\~77%)

# 

# \---

# 

# \## 📸 Screenshots

# 

# \### 🖥️ Web UI

# !\[UI](assets/ui.png)

# 

# \### 📡 API Response

# !\[API](assets/api.png)

# 

# \### 🧪 Test Report

# !\[Tests](assets/tests.png)

# \---

# 

# \## 🔮 Future Improvements

# 

# \* AI-based personalized recommendations

# \* User history tracking dashboard

# \* Carbon footprint trends visualization

# \* Mobile-friendly UI improvements

# 

# \---

# 

# \## 👩‍💻 Author

# 

# Developed by \*\*Devi Sri Sravani\*\*

# 

# \---

# 

# \## 🏁 Project Status

# 

# ✔ Backend Complete

# ✔ API Working

# ✔ Testing Complete

# ✔ Ready for Deployment



