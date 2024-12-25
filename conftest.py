import json
import os
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='session')
def config():
    """Fixture to load configuration from file based on environment."""
    env = os.getenv('TEST_ENV', 'staging')
    config_file_path = f'{os.getcwd()}/config/{env}_config.json'
    with open(config_file_path) as config_file:
        config = json.load(config_file)
    return config

@pytest.fixture
def browser(config):
    """Fixture to provide browser object for tests."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.get(config['base_url'])
    yield driver
    driver.quit()

def pytest_configure():
    """Setup live logging for tests."""
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s | [%(levelname)-7s]: %(message)s")
    logging.getLogger().info("Live logging test setup complete")
