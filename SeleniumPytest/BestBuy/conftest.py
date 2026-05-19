import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config


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

    print("\n========== OPENING BESTBUY WEBSITE ==========")

    driver.get(Config.BASE_URL)

    print("SUCCESS : BestBuy website opened")

    print("\n========== SELECTING COUNTRY ==========")

    usa = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h4[text()='United States']")
        )
    )

    usa.click()

    print("SUCCESS : United States selected")

    time.sleep(5)

    yield driver

    print("\n========== CLOSING BROWSER ==========")

    driver.quit()