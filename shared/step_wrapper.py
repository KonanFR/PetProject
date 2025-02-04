import contextlib
import logging
import allure
logger = logging.getLogger(__name__)

class AllureReporter:
    """Step logger class."""

    @contextlib.contextmanager
    def step(self, step_name: str, browser = None):
        """Create a step in the report."""
        logger.info(f"[STEP]: {step_name} -- started.")
        with allure.step(step_name):
            self.take_screenshot(browser, f"Before - {step_name}")

            yield

            self.take_screenshot(browser, f"After - {step_name}")

        logger.info(f"[STEP]: {step_name} -- finished.")

    @staticmethod
    def take_screenshot(browser, name: str):
        """Helper to take and attach a screenshot."""
        screenshot = browser.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
