import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil


class TVProductsPage:

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
    min_price = (
        By.XPATH,
        "//input[@placeholder='Min Price']"
    )

    max_price = (
        By.XPATH,
        "//input[@placeholder='Max Price']"
    )

    set_button = (
        By.XPATH,
        "//button[.//span[text()='Set']]"
    )

    first_add_to_cart = (
        By.XPATH,
        "(//button[contains(@data-testid,'plp-add-to-cart')])[1]"
    )

    second_add_to_cart = (
        By.XPATH,
        "(//button[contains(@data-testid,'plp-add-to-cart')])[2]"
    )

    continue_shopping = (
        By.XPATH,
        "//a[@data-testid='close-large']"
    )

    go_to_cart = (
        By.XPATH,
        "(//a[@data-testid='go-to-cart'])[2]"
    )

    brand_search_box = (
        By.XPATH,
        "//input[@placeholder='Search Brand']"
    )

    applied_price_filter_checkbox = (
        By.CSS_SELECTOR,
        "input[id='100_to_500']"
    )

    # ==========================================================
    # APPLY BRAND FILTERS
    # ==========================================================
    @allure.step("Apply Brand Filters")
    def apply_brand_filters(self, brands):

        self.logger.info("===================================================")
        self.logger.info(
            "TV PRODUCTS PAGE : APPLY BRAND FILTERS"
        )
        self.logger.info("===================================================")

        # Scroll to brand section
        for i in range(1800, 4200, 300):

            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        # Apply all brand filters
        for brand in brands:

            self.logger.info(
                f"APPLYING BRAND FILTER : {brand}"
            )

            brand_checkbox = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"//input[@id='{brand}']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                brand_checkbox
            )

            self.logger.info(
                f"SUCCESS : {brand} FILTER APPLIED"
            )

            time.sleep(2)

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "brand_filters"
        )

        allure.attach(
            "All selected brand filters applied successfully",
            name="Brand Filter Log",
            attachment_type=allure.attachment_type.TEXT
        )

        self.logger.info(
            "SUCCESS : ALL BRAND FILTERS APPLIED"
        )

    # ==========================================================
    # APPLY PRICE FILTERS
    # ==========================================================
    @allure.step("Apply Price Filters")
    def apply_price_filters(
            self,
            min_val,
            max_val,
            screenshot_name="price_filter"
    ):

        self.logger.info("===================================================")
        self.logger.info(
            f"TV PRODUCTS PAGE : APPLY PRICE FILTER "
            f"{min_val} - {max_val}"
        )
        self.logger.info("===================================================")

        # Enter minimum price
        min_box = self.wait.until(
            EC.element_to_be_clickable(
                self.min_price
            )
        )

        min_box.clear()

        min_box.send_keys(
            str(min_val)
        )

        self.logger.info(
            f"MINIMUM PRICE ENTERED : {min_val}"
        )

        time.sleep(2)

        # Enter maximum price
        max_box = self.wait.until(
            EC.element_to_be_clickable(
                self.max_price
            )
        )

        max_box.clear()

        max_box.send_keys(
            str(max_val)
        )

        self.logger.info(
            f"MAXIMUM PRICE ENTERED : {max_val}"
        )

        time.sleep(2)

        # Click Set button
        set_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.set_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            set_btn
        )

        self.logger.info(
            "SET BUTTON CLICKED"
        )

        time.sleep(10)

        # Refresh page
        self.driver.refresh()

        self.logger.info(
            "PAGE REFRESHED"
        )

        time.sleep(8)

        # Scroll again
        for i in range(1800, 4200, 300):

            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        ScreenshotUtil.capture_screenshot(
            self.driver,
            screenshot_name
        )

        self.logger.info(
            "SUCCESS : PRICE FILTER APPLIED"
        )

        allure.attach(
            f"Price filter applied successfully : "
            f"{min_val} to {max_val}",
            name="Price Filter Log",
            attachment_type=allure.attachment_type.TEXT
        )

    # ==========================================================
    # ADD FIRST TWO PRODUCTS
    # ==========================================================
    @allure.step("Add First Two Products To Cart")
    def add_first_two_products(self):

        self.logger.info("===================================================")
        self.logger.info(
            "TV PRODUCTS PAGE : ADD PRODUCTS TO CART"
        )
        self.logger.info("===================================================")

        # First Product
        first_product = self.wait.until(
            EC.element_to_be_clickable(
                self.first_add_to_cart
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            first_product
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            first_product
        )

        self.logger.info(
            "FIRST PRODUCT ADDED"
        )

        allure.attach(
            "First product added to cart successfully",
            name="Cart Log - 1",
            attachment_type=allure.attachment_type.TEXT
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "first_product_added"
        )

        time.sleep(5)

        # Continue Shopping
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_shopping
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )

        self.logger.info(
            "CONTINUE SHOPPING CLICKED"
        )

        time.sleep(5)

        # Second Product
        second_product = self.wait.until(
            EC.element_to_be_clickable(
                self.second_add_to_cart
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            second_product
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            second_product
        )

        self.logger.info(
            "SECOND PRODUCT ADDED"
        )

        allure.attach(
            "Second product added to cart successfully",
            name="Cart Log - 2",
            attachment_type=allure.attachment_type.TEXT
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "second_product_added"
        )

        self.logger.info(
            "SUCCESS : TWO PRODUCTS ADDED TO CART"
        )

        time.sleep(5)

    # ==========================================================
    # GO TO CART
    # ==========================================================
    @allure.step("Click Go To Cart")
    def click_go_to_cart(self):

        self.logger.info("===================================================")
        self.logger.info(
            "TV PRODUCTS PAGE : GO TO CART"
        )
        self.logger.info("===================================================")

        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.go_to_cart
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "cart_page"
        )

        self.logger.info(
            "SUCCESS : CART PAGE OPENED"
        )

        allure.attach(
            "Cart page opened successfully",
            name="Cart Navigation Log",
            attachment_type=allure.attachment_type.TEXT
        )

        time.sleep(5)

    # ==========================================================
    # INVALID BRAND FILTER
    # ==========================================================
    @allure.step("Apply Invalid Brand Filter")
    def apply_invalid_brand_filter(
            self,
            brand_name
    ):

        self.logger.info("===================================================")
        self.logger.info(
            f"TV PRODUCTS PAGE : INVALID BRAND "
            f"{brand_name}"
        )
        self.logger.info("===================================================")

        # Scroll to brand filter section
        for i in range(1800, 3500, 300):

            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        brand_box = self.wait.until(
            EC.element_to_be_clickable(
                self.brand_search_box
            )
        )

        brand_box.clear()

        brand_box.send_keys(
            brand_name
        )

        self.logger.info(
            f"INVALID BRAND ENTERED : {brand_name}"
        )

        time.sleep(5)

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "invalid_brand"
        )

        self.logger.info(
            "SUCCESS : INVALID BRAND VALIDATION COMPLETED"
        )

        allure.attach(
            f"Invalid brand validation completed for : "
            f"{brand_name}",
            name="Invalid Brand Log",
            attachment_type=allure.attachment_type.TEXT
        )

    # ==========================================================
    # INVALID PRICE FILTER- CLEAR
    # ==========================================================
    def clear_applied_price_filter(self):

        self.logger.info(
            "CLEARING APPLIED PRICE FILTER"
        )

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(2)

        checkbox = self.wait.until(

            EC.element_to_be_clickable(
                self.applied_price_filter_checkbox
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        self.logger.info(
            "PREVIOUS PRICE FILTER REMOVED"
        )

        time.sleep(3)