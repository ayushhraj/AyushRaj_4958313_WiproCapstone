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