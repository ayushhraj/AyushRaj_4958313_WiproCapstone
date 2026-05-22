import os
import time
import allure
import subprocess


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


# ==========================================================
# BEFORE EACH SCENARIO
# ==========================================================
def before_scenario(context, scenario):
    logger.info("\n")
    logger.info("###################################################")
    logger.info(f"STARTED SCENARIO : {scenario.name}")
    logger.info("###################################################")

    # Create screenshots folder
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Browser options
    edge_options = Options()

    edge_options.add_argument(
        "--start-maximized"
    )

    if Config.HEADLESS:
        edge_options.add_argument(
            "--headless"
        )

    # Launch browser
    driver = webdriver.Edge(
        options=edge_options
    )

    driver.implicitly_wait(
        Config.IMPLICIT_WAIT
    )

    wait = WebDriverWait(
        driver,
        Config.EXPLICIT_WAIT
    )

    logger.info(
        "BROWSER LAUNCHED SUCCESSFULLY"
    )

    # Open BestBuy
    driver.get(Config.BASE_URL)

    logger.info(
        "BESTBUY WEBSITE OPENED"
    )

    # Select United States
    usa = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//h4[text()='United States']"
            )
        )
    )

    usa.click()

    logger.info(
        "COUNTRY SELECTED : UNITED STATES"
    )

    time.sleep(5)

    context.driver = driver


# ==========================================================
# AFTER EACH SCENARIO
# ==========================================================
def after_scenario(context, scenario):

    # Capture screenshot on failure
    if scenario.status == "failed":

        screenshot_path = (
            f"screenshots/{scenario.name}.png"
        )

        context.driver.save_screenshot(
            screenshot_path
        )

        allure.attach.file(
            screenshot_path,
            name=scenario.name,
            attachment_type=allure.attachment_type.PNG
        )

        logger.error(
            "SCENARIO FAILED"
        )

    else:

        logger.info(
            "SCENARIO PASSED"
        )

    logger.info(
        f"COMPLETED SCENARIO : {scenario.name}"
    )

    logger.info("CLOSING BROWSER")

    if hasattr(context, "driver"):
        context.driver.quit()

    logger.info("===================================================\n")

# ==========================================================
# AFTER COMPLETE TEST EXECUTION
# ==========================================================
def after_all(context):

    logger.info("===================================================")
    logger.info("TEST EXECUTION COMPLETED")
    logger.info("GENERATING ALLURE REPORT...")
    logger.info("===================================================")

    try:

        # Create reports folder if not present
        if not os.path.exists("reports"):
            os.makedirs("reports")

        # Generate Allure Report
        subprocess.run(
            "allure generate reports/allure-results "
            "-o reports/allure-report --clean",
            shell=True,
            check=True
        )

        logger.info(
            "ALLURE REPORT GENERATED SUCCESSFULLY"
        )

        # Open Allure Report
        subprocess.run(
            "allure open reports/allure-report",
            shell=True,
            check=True
        )

        logger.info(
            "ALLURE REPORT OPENED SUCCESSFULLY"
        )

    except Exception as e:

        logger.error(
            f"FAILED TO GENERATE ALLURE REPORT : {e}"
        )