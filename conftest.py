import json
import os

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


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
    browser = WebDriver()
    browser.get(config['base_url'])
    yield browser
    browser.quit()
