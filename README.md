# README: Automation Testing for K12 Education Application

## Overview
This repository contains the automation testing framework and test cases for the **K12 Education Application**. The purpose of this project is to ensure the quality, reliability, and performance of the application through automated testing. The framework is designed to support functional, regression, and performance testing.

---

## Selenium Test Automation Framework

A robust, maintainable, and scalable test automation framework using Python and Selenium.

## Features

- Page Object Model (POM) design pattern
- Cross-browser testing support (Microsoft Edge, Chrome & Firefox)
- Comprehensive logging
- HTML and Allure test reporting
- Configuration management
- Extensible architecture

## Prerequisites
Before setting up the framework, ensure the following are installed:
- selenium==4.1.0
- pytest==7.1.2
- pytest-html==3.1.1
- allure-pytest==2.9.45
- webdriver-manager==3.5.4
- python-dotenv==0.19.2

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/selenium-framework.git
   cd selenium-framework

---
## Table of Contents
1. [Application Overview](#application-overview)
2. [Testing Scope](#testing-scope)
3. [Framework Details](#framework-details)
4. [Prerequisites](#prerequisites)
5. [Setup Instructions](#setup-instructions)
6. [Running Tests](#running-tests)
7. [Test Reporting](#test-reporting)
8. [Contributing](#contributing)
9. [Contact](#contact)

---

## Application Overview
The **K12 Education Application** is a web-based platform designed to support K-12 education by providing tools for teachers, students, and parents. Key features include:
- Student management
- Assignment and grading systems
- Attendance tracking
- Parent-teacher communication
- Learning resources and tools

---

## Testing Scope
The automation testing covers the following areas:
1. **Functional Testing**: Validating core features such as user login, student management, assignment creation, and grading.
2. **Regression Testing**: Ensuring new updates do not break existing functionality.
3. **Performance Testing**: Evaluating system responsiveness and stability under load.
4. **Cross-Browser Testing**: Verifying compatibility across different browsers (Chrome, Firefox, Safari, etc.).
5. **API Testing**: Testing RESTful APIs for backend services.

---

## Framework Details
The **automation framework** is built using the following tools and technologies:
- 📁 Project Structure
- 📁 TestAutomationFramework
- ├── 📁 tests (Test cases)
  -  ├── test_login.py
  -  ├── test_form_submission.py
  -  ├── test_navigation.py
- ├── 📁 pages (Page Object Model classes)
  -  ├── login_page.py
  -  ├── form_page.py
  -  ├── navigation_page.py
- ├── 📁 config (Configuration files)
  -  ├── config.json
- ├── 📁 utils (Logging, reporting, utilities)
  - ├── logger.py
  - ├── report_generator.py
- ├── 📁 drivers (WebDriver executables)
- ├── 📁 reports (Generated test reports)
- ├── requirements.txt (Dependencies)
- ├── conftest.py (Pytest fixtures & setup)
- ├── README.md

---


---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/k12-education-automation.git
   cd k12-education-automation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and configure browser drivers (e.g., ChromeDriver):
   - Ensure the driver is in your system's PATH.
4. Set up environment variables (if required):
   - Create a `.env` file and add necessary variables (e.g., API keys, credentials).

---

## Running Tests
To execute the test suite, use the following commands:
1. Run all tests:
   ```bash
   pytest tests/
   ```
2. Run specific test modules:
   ```bash
   pytest tests/login_test.py
   ```
3. Run tests with Allure reporting:
   ```bash
   pytest --alluredir=./allure-results
   allure serve ./allure-results
   ```
4. Run performance tests:
   ```bash
   locust -f performance_tests/load_test.py
   ```

---

## Test Reporting
- **Allure Reports**: Generate detailed and interactive test reports.
- **Pytest-html**: Generate HTML reports for quick insights.
- **Logs**: Detailed logs are stored in the `logs/` directory for debugging.

---

## Adding New Tests
Create a new page object in pages/ if needed

Add test file in tests/ following naming convention test_*.py

Use the existing utilities for logging, reporting and driver management

---

## Contributing
We welcome contributions to improve the automation framework. Follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## Sample output or screenshots of the test reports.

![image](https://github.com/user-attachments/assets/74e60df8-3be2-4444-aee1-2dbd6ab44422)

![image](https://github.com/user-attachments/assets/ab3ff28b-717c-47bc-ba1e-c623ab81ab0b)

![image](https://github.com/user-attachments/assets/773906a1-5b86-432f-aada-8842179b6d78)


---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
