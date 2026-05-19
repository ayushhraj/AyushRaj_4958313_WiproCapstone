import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class CartPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = LogGenerator.loggen()

    # ===== LOCATORS =====

    checkout_button = (
        By.XPATH,
        "//button[contains(text(),'Checkout')]"
    )

    email_input = (By.ID, "fld-e")

    continue_button = (
        By.XPATH,
        "//button[contains(text(),'Continue')]"
    )

    # ===== METHODS =====

    def click_checkout(self):

        print("\n========== CLICKING CHECKOUT ==========")

        checkout = self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        )

        checkout.click()

        self.driver.save_screenshot(
            "screenshots/checkout.png"
        )

        allure.attach.file(
            "screenshots/checkout.png",
            name="Checkout Page",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Checkout page opened")

        self.logger.info(
            "SUCCESS : Checkout page opened"
        )

        time.sleep(5)

    def enter_invalid_email(self, invalid_email):

        print("\n========== ENTERING INVALID EMAIL ==========")

        self.logger.info(
            f"STARTED : Entering invalid email {invalid_email}"
        )

        email_box = self.wait.until(
            EC.element_to_be_clickable(
                self.email_input
            )
        )

        email_box.clear()
        email_box.send_keys(invalid_email)

        print(f"Invalid email entered : {invalid_email}")

        self.driver.save_screenshot(
            "screenshots/invalid_email_entered.png"
        )

        time.sleep(3)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        )

        continue_btn.click()

        self.driver.save_screenshot(
            "screenshots/invalid_email_validation.png"
        )

        allure.attach.file(
            "screenshots/invalid_email_validation.png",
            name="Invalid Email Validation",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Invalid email validation completed")

        self.logger.info(
            "SUCCESS : Invalid email validation completed"
        )

        time.sleep(5)