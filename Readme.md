# 📘 Calculator Project with Automated Tests

## 📌 Overview
This project is a **command-line calculator application in Python** that supports the following arithmetic operations:

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division  

It was developed as part of **Assignment 3** to demonstrate **object-oriented programming principles (CLO6)** in Python.  
The project also includes **automated unit tests** and a **CI/CD pipeline** with GitHub Actions.

---

## 🚀 Features
- Interactive **REPL-style** command-line interface  
- Handles **integers, floats, and negative numbers**  
- Clear error handling (e.g., division by zero)  
- Automated unit + parameterized tests with `pytest`  
- Code coverage reports with `pytest-cov`  
- Continuous Integration with **GitHub Actions**  

---

## 🛠️ Project Structure
```text
assignment-3/
├── app/
│   ├── calculator/          # Calculator class (add, subtract, multiply, divide)
│   └── operations/          # (optional: reusable operation functions)
├── tests/                   # Unit & parameterized tests
│   ├── test_calculator.py
│   └── test_units.py
├── main.py                  # REPL entry point
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Project dependencies
└── .github/workflows/
    └── python-app.yml       # GitHub Actions workflow
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/techy-Nik/assignment-3.git
cd assignment-3
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the program:
```bash
python main.py
```

Example session:
```text
Simple Calculator (type 'exit' to quit)
Enter expression (e.g. 2 + 3): 4 * 5
Result: 20.0

Enter expression (e.g. 2 + 3): 10 / 0
Error: Cannot divide by zero

Enter expression (e.g. 2 + 3): exit
Goodbye!
```

---

## 🧪 Running Tests

Run all tests:
```bash
pytest -v
```

Run tests with coverage:
```bash
pytest --cov=app --cov-report=html
```

Open the coverage report in your browser:
```text
htmlcov/index.html
```

---

## 🔄 Continuous Integration (CI)
This project uses **GitHub Actions** for automated testing.  
On each push, it:  
- ✅ Runs all unit + parameterized tests  
- ✅ Verifies code coverage  
- ✅ Ensures code quality  

👉 Check results here: [GitHub Actions](https://github.com/techy-Nik/assignment-3/actions)

---

## 🎯 Learning Outcomes
This project demonstrates:

- ✅ Implementing **object-oriented programming** in Python (CLO6)  
- ✅ Writing **unit and parameterized tests** for complete test coverage  
- ✅ Setting up **Continuous Integration (CI)** with GitHub Actions  
- ✅ Building an **interactive REPL application** with input validation  

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
