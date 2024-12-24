import logging
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

def navigate_to_url(browser: WebDriver, url: str) -> None:
    """Navigate to URL."""
    browser.get(url)

def get_element(browser: WebDriver, selector: tuple, timeout: int = 30) -> WebElement:
    """Waiting for element."""
    if isinstance(selector, tuple):
        logging.info(f"Waiting for element {selector} started.")
        start_time = time.time()
        while time.time() < start_time + timeout:
            try:
                logging.info(f"Trying to find element {selector}.")
                return browser.find_element(*selector)
            except NoSuchElementException:
                logging.info(f"Element {selector} is not found.")
                time.sleep(1)
        raise TimeoutError(f"Element {selector} not found within {timeout} seconds.")
    raise ValueError("Selector should be a tuple")
