# 📘 Python Calculator Project with Automated Tests

## 📌 Overview

This project is a **simple calculator application in Python** that supports basic arithmetic operations using **object-oriented programming principles** (CLO6):

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division

It includes **automated tests** using `pytest` to ensure functionality and correctness.

---

## 🚀 Features

* Command-line interface (REPL style)
* Object-oriented design with the `Operations` class
* Handles negative numbers (e.g., `-5 * -3`)
* Automated testing with `pytest`
* Parameterized tests to cover multiple input scenarios efficiently
* Full code coverage using `pytest-cov`

---

## 🛠️ Project Structure

```text
Assigment3/
│── app/
│   ├── __init__.py
│   ├── calculator/          # REPL logic and Operations import
│   └── operations/          # Operations class (addition, subtraction, multiplication, division)
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py   # Unit tests
│   └── test_units.py        # Parameterized tests
├── main.py                  # REPL entry point
├── requirements.txt         # Project dependencies
└── pytest.ini               # Pytest configuration

```

---

## ▶️ Usage

Run the calculator:

```bash
python main.py
```

Enter expressions like:

```text
number operator number
```

✅ Valid examples:

```text
5 + 3
-5 * -3
10 / 2
```

❌ Invalid (no spaces):

```text
2+-3
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest -v tests/
```

Generate a coverage report:

```bash
pytest --cov=app --cov-report=html
```

Then open:

```text
htmlcov/index.html
```

in your browser.

---

## 🎯 Learning Outcomes

This project demonstrates:

* ✅ Implementing **object-oriented programming principles** in Python (CLO6)
