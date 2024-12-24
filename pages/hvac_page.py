from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from shared.e2e_steps import get_element


class HvacPage:
    """HVAC page object."""
    def __init__(self, browser: WebDriver):
        """Initialize the HVAC page object."""
        self.browser = browser

    page_button = lambda text: (By.XPATH, f'//button[contains(string(), "{text}")]')
    zip_code_label = (By.XPATH, '//label[contains(@for, "zipCode")]')
    zip_code_input = (By.XPATH, '//input[contains(@id, "zipCode")]')
    repair_button = (By.XPATH, '//input[contains(@value, "repair")]/following-sibling::label')
    repair_message_text = "Unfortunately, our contractors only do HVAC replacement. Would you still like to continue?"
    repair_message_locator = (By.XPATH, f'//div[contains(string(), "{repair_message_text}"')
    sorry_message_text = "Sorry to see you go!"
    sorry_message_locator = (By.XPATH, f'//div[contains(string(), "{sorry_message_text}"')

    def fill_zip_code(self, zip_code: str) -> None:
        """Fill in zip code.

        Args:
            zip_code: Zip code to fill in.

        Returns:
            None.
        """
        get_element(self.browser, self.zip_code_label).click()
        get_element(self.browser, self.zip_code_input).send_keys(zip_code)

    def click_on_button(self, selector: Tuple[By, str]) -> None:
        """Click estimate button.

        Args:
            selector: Selector to click.

        Returns:
            None.
        """
        get_element(self.browser, selector).click()

    def check_message(self, message: str) -> None:
        """Check message.

        Args:
            message: Message to check.

        Returns:
            None.
        """
        get_element(self.browser, (By.XPATH, f'//div[contains(string(), "{message}")]'))
