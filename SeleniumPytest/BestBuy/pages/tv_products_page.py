import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class TVProductsPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            Config.EXPLICIT_WAIT
        )

        self.logger = LogGenerator.loggen()

    # LOCATORS

    samsung_checkbox = (By.XPATH, "//input[@id='Samsung']")
    lg_checkbox = (By.XPATH, "//input[@id='LG']")
    sony_checkbox = (By.XPATH, "//input[@id='Sony']")

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

    # add_to_cart_buttons = (
    #     By.XPATH,
    #     "//button[contains(@data-testid,'add-to-cart')]"
    # )

    first_add_to_cart = (
        By.XPATH,
        "(//button[contains(@data-testid,'plp-add-to-cart')])[1]"
    )

    continue_shopping = (
        By.XPATH,
        "//a[@data-testid='close-large']"
    )

    second_add_to_cart = (
        By.XPATH,
        "(//button[contains(@data-testid,'plp-add-to-cart')])[2]"
    )

    go_to_cart = (
        By.XPATH,
        "(//a[@data-testid='go-to-cart'])[2]"
    )

    # METHODS

    def apply_brand_filters(self):
        self.logger.info(
            "Applying Brand Filters"
        )

        print("\n===== APPLYING BRAND FILTERS =====")

        # SCROLL TO PRODUCTS SECTION

        for i in range(1800, 4200, 300):
            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        print("Scrolled to TV products section")

        time.sleep(5)

        # APPLY SAMSUNG

        samsung = self.wait.until(
            EC.element_to_be_clickable(
                self.samsung_checkbox
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            samsung
        )

        print("Samsung selected")

        time.sleep(3)

        # APPLY LG

        lg = self.wait.until(
            EC.element_to_be_clickable(
                self.lg_checkbox
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            lg
        )

        print("LG selected")

        time.sleep(3)

        # APPLY SONY

        sony = self.wait.until(
            EC.element_to_be_clickable(
                self.sony_checkbox
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            sony
        )

        print("Sony selected")

        # WAIT FOR FILTERS

        time.sleep(10)

        # REFRESH

        self.driver.refresh()

        self.logger.info(
            "Page refreshed after brand filters"
        )

        # WAIT AFTER REFRESH

        time.sleep(8)

        # SCROLL TO FILTERED TV PRODUCTS

        print("Scrolling to filtered TV products...")

        for i in range(1800, 4200, 300):
            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.7)

        print("Filter section reached")

        time.sleep(5)

        # SCREENSHOT

        self.driver.save_screenshot(
            "screenshots/brand_filters.png"
        )

        print("SUCCESS: Brand filters applied")

    def apply_price_filters(self, min_val, max_val):
        self.logger.info(
            "Applying Price Filters"
        )

        print("\n===== APPLYING PRICE FILTERS =====")

        # MIN PRICE

        min_box = self.wait.until(
            EC.element_to_be_clickable(
                self.min_price
            )
        )

        min_box.clear()

        min_box.send_keys(str(min_val))

        print(f"Min price entered: {min_val}")

        time.sleep(2)

        # MAX PRICE

        max_box = self.wait.until(
            EC.element_to_be_clickable(
                self.max_price
            )
        )

        max_box.clear()

        max_box.send_keys(str(max_val))

        print(f"Max price entered: {max_val}")

        time.sleep(2)

        # CLICK SET BUTTON

        set_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.set_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            set_btn
        )

        print("Set button clicked")

        # WAIT FOR PRICE FILTERS

        time.sleep(10)

        # REFRESH PAGE

        self.driver.refresh()

        self.logger.info(
            "Page refreshed after price filters"
        )

        # WAIT AFTER REFRESH

        time.sleep(8)

        # SCROLL DOWN TO FILTERED TV RESULTS

        print("Scrolling to filtered TV results...")

        for i in range(1800, 4200, 300):
            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        print("Filtered TV products visible")

        time.sleep(5)

        # SCREENSHOT

        self.driver.save_screenshot(
            "screenshots/price_filters.png"
        )

        print("SUCCESS: Price filters applied")

    def add_first_two_products(self):

        self.logger.info(
            "Adding first product"
        )

        # FIRST PRODUCT

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
            "First product added"
        )

        self.driver.save_screenshot(
            "screenshots/first_product_added.png"
        )

        time.sleep(5)

        # CONTINUE SHOPPING

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
            "Continue shopping clicked"
        )

        time.sleep(5)

        # SECOND PRODUCT

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
            "Second product added"
        )

        self.driver.save_screenshot(
            "screenshots/second_product_added.png"
        )

        time.sleep(5)

    def click_go_to_cart(self):

        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.go_to_cart
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

        self.logger.info(
            "Navigated to cart"
        )

        self.driver.save_screenshot(
            "screenshots/cart_page.png"
        )

        time.sleep(5)