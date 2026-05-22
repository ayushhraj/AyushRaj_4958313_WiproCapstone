import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil


class TopDealsPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = LogGenerator.loggen()

    tv_home_theater = (
        By.XPATH,
        "//*[contains(text(),'TV & Home Theater')]"
    )

    def click_tv_home_theater(self):

        tv = self.wait.until(
            EC.element_to_be_clickable(
                self.tv_home_theater
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            tv
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "tv_home_theater"
        )

        self.logger.info(
            "SUCCESS : TV & Home Theater opened"
        )

        time.sleep(5)