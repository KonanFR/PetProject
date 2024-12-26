from pages.hvac_page import HvacPage
from shared.e2e_steps import assert_equal
import pytest

from shared.step_logger import StepLogger


class TestHomeBuddyPage:
    """Tests for the HomeBuddy page."""

    def test_contractor_not_found_flow(self, browser):
        """Test the HomeBuddy page."""
        hvac_page = HvacPage(browser)

        with StepLogger("When user fill zip code and click on 'Get estimate' button"):
            hvac_page.fill_input("10001", "zipCode", "zipCode")
            hvac_page.click_on_button(HvacPage.button("Get estimate"))

        with StepLogger("When user clicks on 'Repair' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Repair"))
            hvac_page.check_message(hvac_page.repair_message_text)
            hvac_page.click_on_button(HvacPage.button("Yes"))

        with StepLogger("When user clicks on 'Air conditioner' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Air conditioner"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Less than 5 years' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Less than 5 "))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Detached' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Detached"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user fills input and clicks 'Next' button"):
            hvac_page.fill_input("300", "squareFeet", "squareFeet")
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Yes' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Yes"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user fills 'Full Name' and 'Email' fields and clicks 'Next' button"):
            hvac_page.fill_input("Sam Smith", "fullName", "fullName")
            hvac_page.fill_input("test@email.com", "email", "email")
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user fills incorrect phone number and clicks 'Submit my request' button"):
            hvac_page.fill_input("800224132", "phoneNumber", "phoneNumber")
            hvac_page.click_on_button(HvacPage.button("Submit my request"))

        with StepLogger("Then validation message is displaying"):
            hvac_page.check_field_validation_message("Phone number must be 10 digits long.", "phoneNumber")

        with StepLogger("When user fills correct phone number and clicks 'Submit my request' button"):
            hvac_page.fill_input("8002241329", "phoneNumber", "phoneNumber", True)
            hvac_page.click_on_button(HvacPage.button("Submit my request"))

        with StepLogger("Then 'Go to homepage' button displaying"):
            hvac_page.check_message(hvac_page.searching_message, to_disappear=True)

        with StepLogger("When user clicks on 'Go to homepage' button"):
            hvac_page.click_on_button(HvacPage.button("Go to homepage"))

        with StepLogger("Then correct page opened"):
            assert_equal("https://hb-autotests.stage.sirenltd.dev/", browser.current_url, "URL is not correct")

    @pytest.mark.parametrize("test_data", [
        ("BrandonFaircloth", "testemail.com", "Full name must be written in English letters and dashes if needed."),
        ("Veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeery looooooooooooooooooooong", "test@email",
         "Full name can’t be longer than 64 characters.")
    ])
    def test_get_contractor_flow_wrong_name_email(self, browser, test_data):
        """Test the HomeBuddy page."""
        hvac_page = HvacPage(browser)

        with StepLogger("When user fill zip code and click on 'Get estimate' button"):
            hvac_page.fill_input("10001", "zipCode", "zipCode")
            hvac_page.click_on_button(HvacPage.button("Get estimate"))

        with StepLogger("When user clicks on 'Replacement' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Replacement"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Water heater' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Water heater"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Propane' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Propane"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on '5 to 10 years' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("5 to 10"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Detached' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Detached"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user selects 'Not sure' checkbox and clicks 'Next' button"):
            hvac_page.click_on_button(HvacPage.checkbox("Not sure"))
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("When user clicks on 'Yes' tile and 'Next' button"):
            hvac_page.click_on_button(HvacPage.tile_button("Yes"))
            hvac_page.click_on_button(HvacPage.button("Next"))

            name, email, validation_message = test_data

        with StepLogger("When user fills incorrect 'Full Name' and 'Email' fields and clicks 'Next' button"):
            hvac_page.fill_input(name, "fullName", "fullName")
            hvac_page.fill_input(email, "email", "email")
            hvac_page.click_on_button(HvacPage.button("Next"))

        with StepLogger("Then validation messages is displaying"):
            hvac_page.check_field_validation_message(validation_message,"fullName")
            hvac_page.check_field_validation_message("Must be a valid email address.", "email")
