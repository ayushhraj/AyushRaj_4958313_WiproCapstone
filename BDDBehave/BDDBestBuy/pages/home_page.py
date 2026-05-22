import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator
from utilities.screenshot_utils import ScreenshotUtil


class HomePage:

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
    top_deals = (
        By.XPATH,
        "(//*[contains(text(),'Top Deals')])[1]"
    )

    # ==========================================================
    # CLICK TOP DEALS
    # ==========================================================
    @allure.step("Click Top Deals Section")
    def click_top_deals(self):

        self.logger.info("===================================================")
        self.logger.info("HOME PAGE : CLICK TOP DEALS")
        self.logger.info("===================================================")

        top = self.wait.until(
            EC.element_to_be_clickable(
                self.top_deals
            )
        )

        top.click()

        self.logger.info(
            "SUCCESS : TOP DEALS CLICKED"
        )

        allure.attach(
            "Top Deals section clicked successfully",
            name="Execution Log",
            attachment_type=allure.attachment_type.TEXT
        )

        ScreenshotUtil.capture_screenshot(
            self.driver,
            "top_deals_page"
        )

        time.sleep(5)