import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


class TopDealsPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            Config.EXPLICIT_WAIT
        )

        self.logger = LogGenerator.loggen()

    # LOCATOR

    tv_home_theater = (
        By.XPATH,
        "//*[contains(text(),'TV & Home Theater')]"
    )

    # METHOD

    def click_tv_home_theater(self):

        self.logger.info(
            "Clicking TV & Home Theater"
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

        self.logger.info(
            "TV & Home Theater clicked successfully"
        )

        time.sleep(5)