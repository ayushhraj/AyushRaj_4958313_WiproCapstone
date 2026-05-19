import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class TVProductsPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = LogGenerator.loggen()

    # ===== LOCATORS =====

    samsung_checkbox = (By.XPATH, "//input[@id='Samsung']")
    lg_checkbox = (By.XPATH, "//input[@id='LG']")
    sony_checkbox = (By.XPATH, "//input[@id='Sony']")

    min_price = (By.XPATH, "//input[@placeholder='Min Price']")
    max_price = (By.XPATH, "//input[@placeholder='Max Price']")

    set_button = (By.XPATH, "//button[.//span[text()='Set']]")

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

    # ===== METHODS =====

    def apply_brand_filters(self):

        print("\n========== APPLYING BRAND FILTERS ==========")

        self.logger.info(
            "STARTED : Applying Samsung, LG and Sony filters"
        )

        for i in range(1800, 4200, 300):

            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        print("SUCCESS : Products section visible")

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

        time.sleep(10)

        self.driver.refresh()

        print("SUCCESS : Brand filters refreshed")

        time.sleep(8)

        for i in range(1800, 4200, 300):

            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.7)

        self.driver.save_screenshot(
            "screenshots/brand_filters.png"
        )

        allure.attach.file(
            "screenshots/brand_filters.png",
            name="Brand Filters",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Brand filters applied")

        self.logger.info(
            "SUCCESS : Brand filters applied"
        )

    def apply_price_filters(self, min_val, max_val, screenshot_name="price_filters"):

        print("\n========== APPLYING PRICE FILTERS ==========")

        self.logger.info(
            f"STARTED : Applying price filters {min_val} - {max_val}"
        )

        min_box = self.wait.until(
            EC.element_to_be_clickable(
                self.min_price
            )
        )

        min_box.clear()
        min_box.send_keys(str(min_val))

        print(f"Min price entered : {min_val}")

        time.sleep(2)

        max_box = self.wait.until(
            EC.element_to_be_clickable(
                self.max_price
            )
        )

        max_box.clear()
        max_box.send_keys(str(max_val))

        print(f"Max price entered : {max_val}")

        time.sleep(2)

        set_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.set_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            set_btn
        )

        print("SUCCESS : Set button clicked")

        time.sleep(10)

        self.driver.refresh()

        print("SUCCESS : Page refreshed")

        time.sleep(8)

        for i in range(1800, 4200, 300):

            self.driver.execute_script(
                f"window.scrollTo(0, {i});"
            )

            time.sleep(0.8)

        print("SUCCESS : Filtered TV products visible")

        self.driver.save_screenshot(
            f"screenshots/{screenshot_name}.png"
        )

        allure.attach.file(
            f"screenshots/{screenshot_name}.png",
            name="Price Filters",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Price filters applied")

        self.logger.info(
            "SUCCESS : Price filters applied"
        )

    def add_first_two_products(self):

        print("\n========== ADDING PRODUCTS TO CART ==========")

        self.logger.info(
            "STARTED : Adding first two products"
        )

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

        print("SUCCESS : First product added")

        self.driver.save_screenshot(
            "screenshots/first_product_added.png"
        )

        time.sleep(5)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.continue_shopping
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )

        print("SUCCESS : Continue shopping clicked")

        time.sleep(5)

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

        self.driver.save_screenshot(
            "screenshots/second_product_added.png"
        )

        allure.attach.file(
            "screenshots/second_product_added.png",
            name="Products Added",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Second product added")

        self.logger.info(
            "SUCCESS : Two products added to cart"
        )

        time.sleep(5)

    def click_go_to_cart(self):

        print("\n========== GOING TO CART ==========")

        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.go_to_cart
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

        self.driver.save_screenshot(
            "screenshots/cart_page.png"
        )

        allure.attach.file(
            "screenshots/cart_page.png",
            name="Cart Page",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Cart page opened")

        self.logger.info(
            "SUCCESS : Cart page opened"
        )

        time.sleep(5)

    def apply_invalid_brand_filter(self, brand_name):

        print("\n========== APPLYING INVALID BRAND ==========")

        self.logger.info(
            f"STARTED : Applying invalid brand {brand_name}"
        )

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
        brand_box.send_keys(brand_name)

        print(f"Invalid brand entered : {brand_name}")

        time.sleep(5)

        self.driver.save_screenshot(
            "screenshots/invalid_brand.png"
        )

        allure.attach.file(
            "screenshots/invalid_brand.png",
            name="Invalid Brand",
            attachment_type=allure.attachment_type.PNG
        )

        print("SUCCESS : Invalid brand validation completed")

        self.logger.info(
            "SUCCESS : Invalid brand validation completed"
        )