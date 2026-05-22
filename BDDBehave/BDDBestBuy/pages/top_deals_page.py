import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil


class TopDealsPage:

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
    tv_home_theater = (
        By.XPATH,
        "//*[contains(text(),'TV & Home Theater')]"
    )

    # ==========================================================
    # CLICK TV & HOME THEATER
    # ==========================================================
    @allure.step("Click TV & Home Theater Section")
    def click_tv_home_theater(self):

        self.logger.info("===================================================")
        self.logger.info(
            "TOP DEALS PAGE : OPEN TV & HOME THEATER"
        )
        self.logger.info("===================================================")

        tv = self.wait.until(
            EC.element_to_be_clickable(
                self.tv_home_theater
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            tv
        )

        self.logger.info(
            "SUCCESS : TV & HOME THEATER OPENED"
        )

        allure.attach(
            "TV & Home Theater section opened successfully",
            name="Execution Log",
            attachment_type=allure.attachment_type.TEXT
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "tv_home_theater"
        )

        time.sleep(5)