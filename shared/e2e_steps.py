import logging
import time
from typing import Union, Any

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


def get_element(
        driver: WebDriver,
        selector: tuple,
        timeout: int = 60,
        to_disappear: bool = False
) -> Union[WebElement, None]:
    """Waiting for element."""
    if isinstance(selector, tuple):
        logger.info(f"Waiting for element {selector} started.")

        start_time = time.time()
        while time.time() < start_time + timeout:
            try:
                if webdriver_wait(driver, selector, timeout, to_disappear):
                    logger.info(f"Trying to find element {selector}.")
                    return driver.find_element(*selector)
                # to_disappear=True
                return
            except NoSuchElementException:
                logger.info(f"Element {selector} is not found.")
                time.sleep(1)
        raise TimeoutError(f"Element {selector} not found within {timeout} seconds.")
    raise ValueError("Selector should be a tuple")


def webdriver_wait(driver: WebDriver, selector: tuple, timeout: int = 30, to_disappear: bool = False) -> bool:
    """Return True if element is present on the DOM, False otherwise."""
    by = selector[0]
    locator = selector[1]
    message = f"Failed on element: '{locator}', by '{by}'"

    if to_disappear:
        logger.info(f"Check if element '{selector}' is either invisible or not present on the DOM.")
        condition = ec.invisibility_of_element_located((by, locator))
        WebDriverWait(driver, timeout, ignored_exceptions=[StaleElementReferenceException]
                      ).until(condition, message=message)
        return False

    else:
        logger.info(f"Check if element '{locator}' is present on the DOM of a page")
        condition = ec.presence_of_element_located((by, locator))

    WebDriverWait(driver, timeout, ignored_exceptions=[StaleElementReferenceException]
                  ).until(condition, message=message)
    return True

def assert_equal(expected: Any, actual: Any, extra_message: str = "") -> None:
    """Assert equal."""
    default_message = f"Expected: {expected}, got: {actual}."
    message = f"{extra_message}. {default_message}" if extra_message else default_message
    assert expected == actual, message

def assert_condition(condition: bool, extra_message: str = "") -> None:
    """Assert condition."""
    assert condition, extra_message
