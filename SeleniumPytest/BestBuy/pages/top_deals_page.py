import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class TopDealsPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = LogGenerator.loggen()

    # ===== LOCATORS =====

    tv_home_theater = (
        By.XPATH,
        "//*[contains(text(),'TV & Home Theater')]"
    )

    # ===== METHODS =====

    def click_tv_home_theater(self):

        print("\n========== OPENING TV & HOME THEATER ==========")

        self.logger.info(
            "STARTED : Opening TV & Home Theater"
        )

        tv = self.wait.until(
            EC.element_to_be_clickable(
                self.tv_home_theater
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            tv
        )

        self.driver.save_screenshot(
            "screenshots/tv_home_theater.png"
        )

        print("SUCCESS : TV & Home Theater page opened")

        self.logger.info(
            "SUCCESS : TV & Home Theater opened"
        )

        time.sleep(5)