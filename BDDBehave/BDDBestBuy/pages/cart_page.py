import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            Config.EXPLICIT_WAIT
        )

        self.logger = LogGenerator.loggen()

    # ==========================================================
    # LOCATORS
    # ==========================================================
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

    # ==========================================================
    # CLICK CHECKOUT
    # ==========================================================
    @allure.step("Click Checkout")
    def click_checkout(self):

        self.logger.info("===================================================")
        self.logger.info(
            "CART PAGE : CLICK CHECKOUT"
        )
        self.logger.info("===================================================")

        checkout = self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button
            )
        )

        checkout.click()

        self.logger.info(
            "CHECKOUT BUTTON CLICKED"
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "checkout_page"
        )

        self.logger.info(
            "SUCCESS : CHECKOUT PAGE OPENED"
        )

        allure.attach(
            "Checkout page opened successfully",
            name="Checkout Log",
            attachment_type=allure.attachment_type.TEXT
        )

        time.sleep(5)

    # ==========================================================
    # ENTER INVALID EMAIL
    # ==========================================================
    @allure.step("Enter Invalid Email")
    def enter_invalid_email(
            self,
            invalid_email
    ):

        self.logger.info("===================================================")
        self.logger.info(
            f"CART PAGE : ENTER INVALID EMAIL "
            f"{invalid_email}"
        )
        self.logger.info("===================================================")

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
            f"INVALID EMAIL ENTERED : {invalid_email}"
        )

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

        self.logger.info(
            "CONTINUE BUTTON CLICKED"
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "invalid_email_validation"
        )

        self.logger.info(
            "SUCCESS : INVALID EMAIL VALIDATION COMPLETED"
        )

        allure.attach(
            f"Invalid email validation completed for : "
            f"{invalid_email}",
            name="Invalid Email Log",
            attachment_type=allure.attachment_type.TEXT
        )

        time.sleep(5)

    # ==========================================================
    # INCREASE PRODUCT QUANTITY
    # ==========================================================
    @allure.step("Increase Product Quantity")
    def increase_product_quantity(
            self,
            quantity="2"
    ):

        self.logger.info("===================================================")
        self.logger.info(
            f"CART PAGE : UPDATE QUANTITY TO {quantity}"
        )
        self.logger.info("===================================================")

        quantity_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//select[contains(@id,'quantity')])[1]"
                )
            )
        )

        select_quantity = Select(
            quantity_dropdown
        )

        select_quantity.select_by_visible_text(
            quantity
        )

        self.logger.info(
            f"QUANTITY UPDATED TO : {quantity}"
        )

        time.sleep(5)

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "updated_product_quantity"
        )

        updated_quantity = (
            select_quantity.first_selected_option.text
        )

        self.logger.info(
            f"SUCCESS : PRODUCT QUANTITY "
            f"UPDATED TO {updated_quantity}"
        )

        allure.attach(
            f"Product quantity updated successfully to : "
            f"{updated_quantity}",
            name="Quantity Update Log",
            attachment_type=allure.attachment_type.TEXT
        )

        return updated_quantity