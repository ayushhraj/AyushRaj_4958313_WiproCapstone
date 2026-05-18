import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            Config.EXPLICIT_WAIT
        )

        self.logger = LogGenerator.loggen()

    # LOCATORS

    top_deals = (
        By.XPATH,
        "(//*[contains(text(),'Top Deals')])[1]"
    )

    # METHODS

    def click_top_deals(self):

        self.logger.info("Clicking Top Deals")

        top = self.wait.until(
            EC.element_to_be_clickable(
                self.top_deals
            )
        )

        top.click()

        self.driver.save_screenshot(
            "screenshots/top_deals.png"
        )

        self.logger.info("Top Deals clicked successfully")

        time.sleep(5)