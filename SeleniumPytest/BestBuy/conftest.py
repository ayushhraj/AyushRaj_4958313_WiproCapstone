import pytest
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config


@pytest.fixture()
def setup():

    edge_options = Options()

    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    driver.get(Config.BASE_URL)

    # SELECT USA

    usa = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h4[text()='United States']")
        )
    )

    usa.click()

    time.sleep(5)

    yield driver

    driver.quit()