import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            Config.EXPLICIT_WAIT
        )

        self.logger = LogGenerator.loggen()

    checkout_button = (
        By.XPATH,
        "//button[contains(text(),'Checkout')]"
    )

    email_input = (
        By.ID,
        "fld-e"
    )

    continue_button = (
        By.XPATH,
        "//button[contains(text(),'Continue')]"
    )

    def click_checkout(self):

        checkout = self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        )

        checkout.click()

        self.driver.save_screenshot(
            "screenshots/checkout.png"
        )

        self.logger.info(
            "Checkout clicked successfully"
        )

        time.sleep(5)

    def enter_invalid_email(self, invalid_email):
        self.logger.info(
            "Entering invalid email"
        )

        email_box = self.wait.until(
            EC.element_to_be_clickable(
                self.email_input
            )
        )

        email_box.clear()

        email_box.send_keys(
            invalid_email
        )

        self.logger.info(
            f"Invalid email entered: {invalid_email}"
        )

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

        self.logger.info(
            "Continue button clicked"
        )

        self.driver.save_screenshot(
            "screenshots/invalid_email_validation.png"
        )

        time.sleep(5)