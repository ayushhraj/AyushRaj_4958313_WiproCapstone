# 🛒 BestBuy Automation Framework

Selenium automation framework developed for automating the BestBuy E-Commerce website using Python, Selenium WebDriver, Pytest, Page Object Model (POM), Data-Driven Testing, Logging, Screenshots, and Allure Reporting.

---

# 🚀 Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Allure Reports
- OpenPyXL
- HTML Reports
- Edge Browser

---

# 📂 Project Structure

```text
BestBuy/
│
├── config/
│   └── config.py
│
├── pages/
│   ├── home_page.py
│   ├── top_deals_page.py
│   ├── tv_products_page.py
│   └── cart_page.py
│
├── tests/
│   ├── test_bestbuy_workflow.py
│   └── test_positive_negative_tc.py
│
├── utilities/
│   ├── excel_utils.py
│   ├── logger.py
│   └── screenshot_utils.py
│
├── screenshots/
│
├── reports/
│   ├── report.html
│   └── allure-results/
│
├── test_data/
│   └── test_data.xlsx
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ✅ Framework Features

- Page Object Model (POM)
- Data-Driven Testing using Excel
- Parameterized Testing
- Screenshot Utility
- Logging Support
- HTML Reports
- Allure Reporting
- Reusable Utility Methods
- End-to-End Workflow Automation

---

# 🧪 Automated Test Scenarios

## Positive Test Cases
- Apply valid brand filters
- Apply valid price filters
- Add products to cart
- Increase product quantity in cart
- Navigate to checkout page

## Negative Test Cases
- Apply invalid brand filter
- Apply invalid price filter
- Enter invalid email during checkout



---

# ▶️ Run Tests

## Run All Tests
```bash
pytest -v -s
```

## Run Specific Test File
```bash
pytest -v -s tests/test_positive_negative_tc.py
```

## Run Specific Test Case
```bash
pytest -v -s tests/test_positive_negative_tc.py -k "test_increase_product_quantity"
```



# 🔥 Concepts Implemented

- Selenium Automation
- Pytest Framework
- Explicit Waits
- POM Architecture
- Logging
- Screenshot Handling
- Allure Reporting
- Data-Driven Testing
- Parameterization

---

# 👨‍💻 Author

Ayush Raj

GitHub:
https://github.com/ayushhraj