# ITCS386 - Test-Driven Development (TDD) Lab

This repository contains the coursework, lab exercises, and implementation tasks for **ITCS386: Test-Driven Development**. The project focuses on applying core TDD cycles (Red-Green-Refactor), writing comprehensive unit and integration tests, and maintaining high test coverage and clean code quality.

---

## 📌 Project Overview

- **Course:** ITCS386 
- **Topic:** Test-Driven Development (TDD), Unit Testing, and Refactoring
- **Primary Language:** Python 3.10+ *(or Java / TypeScript depending on your stack)*
- **Testing Framework:** `pytest` *(or JUnit 5 / Jest)*

---

## 🔄 TDD Workflow

Development in this repository strictly adheres to the standard TDD lifecycle:

1. **🔴 Red:** Write a failing test that defines a specific feature or requirement.
2. **🟢 Green:** Implement the minimal amount of code needed to make the test pass.
3. **🔵 Refactor:** Clean up the implementation and test code while ensuring all tests continue to pass.

---

## 📂 Project Structure

```text
itcs386-tdd/
├── src/                  # Application source code
│   ├── __init__.py
│   └── calculator.py     # Example business logic module
├── tests/                # Automated test suites
│   ├── __init__.py
│   └── test_calculator.py
├── .gitignore
├── requirements.txt      # Project dependencies
└── README.md