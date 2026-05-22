import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


@pytest.fixture()
def setup():

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    edge_options = Options()
    edge_options.add_argument("--start-maximized")

    if Config.HEADLESS:
        edge_options.add_argument("--headless")

    driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    logger.info("Opening BestBuy website")

    driver.get(Config.BASE_URL)

    usa = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h4[text()='United States']")
        )
    )

    usa.click()

    logger.info("United States selected")

    time.sleep(5)

    yield driver

    logger.info("Closing browser\n")

    driver.quit()

def pytest_unconfigure(config):

    print("\n==========================================")
    print("TESTS COMPLETED SUCCESSFULLY")
    print("GENERATING ALLURE REPORT...")
    print("==========================================\n")

    # Generate permanent Allure Report
    os.system(
        "allure generate reports/allure-results "
        "-o reports/allure-report --clean"
    )

    # Open Allure Report automatically
    os.system(
        "allure open reports/allure-report"
    )