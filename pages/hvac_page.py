from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from shared.e2e_steps import get_element


class HvacPage:
    """HVAC page object."""
    def __init__(self, browser: WebDriver):
        """Initialize the HVAC page object."""
        self.browser = browser

    button = lambda text: (
        By.XPATH, f'//*[contains(@class, "customButton__text") and contains(string(), "{text}")]'
                  f'//ancestor::*[contains(@class, "customButton")]')
    page_button = lambda text: (By.XPATH, f'//button[contains(string(), "{text}")]')
    label_element = lambda for_attr: (By.XPATH, f'//label[contains(@for, "{for_attr}")]')
    input_element = lambda id_attr: (By.XPATH, f'//input[contains(@id, "{id_attr}")]')
    tile_button = lambda text: (By.XPATH, f'//input/following-sibling::label[contains(string(), "{text}")]')
    repair_message_text = "Unfortunately, our contractors only do HVAC replacement. Would you still like to continue?"
    searching_message = "We are searching for a contractor for you..."
    repair_message_locator = (By.XPATH, f'//div[contains(string(), "{repair_message_text}"')
    message_selector = lambda message: (By.XPATH, f'//div[contains(string(), "{message}")]')
    checkbox = lambda text: (By.XPATH, f'//input/following-sibling::label[contains(string(), "{text}")]')
    validation_message = lambda text, for_attr: (
        By.XPATH, f'//div[contains(string(), "{text}")]//ancestor::div[contains(@data-status, "invalid")]'
                  f'//label[contains(@for, "{for_attr}")]'
    )

    def fill_input(self, text: str, label_attr: str, id_attr: str) -> None:
        """Fill in zip code.

        Args:
            text: Zip code to fill in.
            label_attr: Label for the input.
            id_attr: ID attribute for the input.

        Returns:
            None.
        """
        get_element(self.browser, HvacPage.label_element(label_attr)).click()
        get_element(self.browser, HvacPage.input_element(id_attr)).send_keys(text)

    def click_on_button(self, selector: Tuple[By, str]) -> None:
        """Click estimate button.

        Args:
            selector: Selector to click.

        Returns:
            None.
        """
        get_element(self.browser, selector).click()

    def check_message(self, message: str, to_disappear: bool = False) -> None:
        """Check message.

        Args:
            message: Message to check.
            to_disappear: Check if message disappears.

        Returns:
            None.
        """
        get_element(self.browser, HvacPage.message_selector(message), to_disappear=to_disappear)

    def check_field_validation_message(self, message: str, attr_value: str) -> None:
        """Check field validation message.

        Args:
            message: Validation message to check.
            attr_value: Value of the @for attribute for the element's field.

        Returns:
            None.
        """
        assert get_element(self.browser, HvacPage.validation_message(message, attr_value), timeout=10), \
                "Validation message not found!"
