# Project 1: Password Strength Checker

## DecodeLabs Cyber Security Internship

This repository contains my implementation of **Project 1** for the DecodeLabs Cyber Security Internship. The project evaluates the strength of a password based on common cybersecurity best practices.

---

# Project Overview

- **Goal:** Determine whether a password is Weak, Medium, or Strong.
- **Language:** Python
- **Concepts Covered:** String Handling, Conditional Statements, Password Security

---

# Features

- Checks password length.
- Detects uppercase letters.
- Detects lowercase letters.
- Detects numbers.
- Detects special characters.
- Displays password strength.
- Suggests missing security requirements.

---

# Password Strength Criteria

A password is evaluated based on:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

---

# Security Logic

The program assigns a score based on the presence of required password components.

Score = Number of satisfied security requirements

- **Score = 4** → Strong
- **Score = 2–3** → Medium
- **Score = 0–1** → Weak

---

# File Structure

```
Password-Strength-Checker-Decodelabs/
│
├── password_checker.py
└── README.md
```

---

# How to Run

```bash
python3 password_checker.py
```

---

# Example

### Input

```
Password@123
```

### Output

```
RESULT : PASS
STRENGTH : STRONG - Absolute Precision Secured
```

---

# Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

---

# Learning Outcomes

- Understand password security principles.
- Learn conditional logic in Python.
- Validate user input.
- Improve cybersecurity programming skills.

---


DecodeLabs Cyber Security Internship – Week 1 Project
