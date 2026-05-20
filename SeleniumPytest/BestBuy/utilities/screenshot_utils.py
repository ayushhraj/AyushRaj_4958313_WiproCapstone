import os
import allure

from datetime import datetime

from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


class ScreenshotUtil:

    @staticmethod
    def capture_screenshot(driver, screenshot_name="screenshot"):

        screenshot_dir = "screenshots"

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        clean_name = screenshot_name.replace(" ", "_")

        screenshot_path = (
            f"{screenshot_dir}/"
            f"{clean_name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=clean_name,
            attachment_type=allure.attachment_type.PNG
        )

        logger.info(
            f"Screenshot captured: {screenshot_path}"
        )

        return screenshot_path