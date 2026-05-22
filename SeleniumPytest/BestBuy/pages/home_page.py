import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil


class HomePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = LogGenerator.loggen()

    top_deals = (By.XPATH, "(//*[contains(text(),'Top Deals')])[1]")

    def click_top_deals(self):

        top = self.wait.until(
            EC.element_to_be_clickable(self.top_deals)
        )

        top.click()

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "top_deals"
        )

        self.logger.info(
            "SUCCESS : Top Deals opened"
        )

        time.sleep(5)