# Playwright Test Automation for Automation-Exercise Website

## 📌 Project Overview

This project contains automated tests using Playwright and Pytest.

## 🚀 Setup Instructions

1️⃣ **Create a Virtual Environment**

Run the following command to create and activate a virtual environment:

Windows:
```
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```
python -m venv venv
source venv/bin/activate
```

2️⃣ **Install Dependencies**

Run the following command to install required packages:

```
pip install -r requirements.txt`
```

3️⃣ **Run Playwright Install**

Ensure Playwright browsers are installed:

```
playwright install
```
## 🛠 Configuring pytest.ini

The **pytest.ini** file is used to configure Pytest settings. You can customize test execution options, logging, and report generation.


## 🏃 Running Tests

Run All Tests

```
pytest
```

## 📊 Viewing Test Results

**HTML Report:** Open `reports/test_report.html` in a browser.

**Playwright Trace Viewer:** If tests fail, Playwright saves traces in `test-results/`.
Run the command below to view them:
```
playwright show-trace test-results/tests-test-script-py-test-cart-chromium/trace.zip
```