# BestBuy BDD Automation Framework

This project is an automated testing framework developed for the BestBuy web application using **Selenium**, **Python**, **Behave BDD**, and **Allure Reports**.

The framework follows the **Page Object Model (POM)** design pattern and supports:
- End-to-End workflow testing
- Positive and Negative test scenarios
- Screenshot capturing
- Logging
- Allure reporting

---

# Tech Stack

- Python
- Selenium WebDriver
- Behave (BDD)
- Allure Reports
- Page Object Model (POM)
- OpenPyXL
- Logging

---

# Project Structure

```text
BDDBestBuy/
│
├── features/
│   ├── end_to_end.feature
│   ├── positive_negative.feature
│   ├── environment.py
│   │
│   └── steps/
│       ├── end_to_end_steps.py
│       └── positive_negative_steps.py
│
├── pages/
│   ├── home_page.py
│   ├── top_deals_page.py
│   ├── tv_products_page.py
│   └── cart_page.py
│
├── utilities/
│   ├── logger.py
│   ├── screenshot_utils.py
│   └── excel_utils.py
│
├── config/
│   └── config.py
│
├── testdata/
│   └── bestbuy_testdata.xlsx
│
├── logs/
│   └── automation.log
│
├── reports/
│   ├── allure-results/
│   └── allure-report/
│
├── screenshots/
│
├── behave.ini
├── requirements.txt
└── README.md