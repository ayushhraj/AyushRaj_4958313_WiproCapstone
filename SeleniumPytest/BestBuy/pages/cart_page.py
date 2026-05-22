import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil
from selenium.webdriver.support.ui import Select

class CartPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = LogGenerator.loggen()

    checkout_button = (
        By.XPATH,
        "//button[contains(text(),'Checkout')]"
    )

    email_input = (By.ID, "fld-e")

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

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "checkout_page"
        )

        self.logger.info(
            "SUCCESS : Checkout page opened"
        )

        time.sleep(5)

    def enter_invalid_email(self, invalid_email):

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

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "invalid_email_entered"
        )

        time.sleep(3)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        )

        continue_btn.click()

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "invalid_email_validation"
        )

        self.logger.info(
            "SUCCESS : Invalid email validation completed"
        )

        time.sleep(5)



    def increase_product_quantity(self, quantity="2"):
        self.logger.info(
            f"STARTED : Updating product quantity to {quantity}"
        )

        quantity_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//select[contains(@id,'quantity')])[1]"
                )
            )
        )

        select_quantity = Select(quantity_dropdown)

        select_quantity.select_by_visible_text(quantity)

        time.sleep(5)

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "updated_product_quantity"
        )

        updated_quantity = (
            select_quantity.first_selected_option.text
        )

        self.logger.info(
            f"SUCCESS : Product quantity updated to {updated_quantity}"
        )

        return updated_quantity