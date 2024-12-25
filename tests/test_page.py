from pages.hvac_page import HvacPage
from shared.e2e_steps import assert_equal


class TestHomeBuddyPage:
    """Tests for the HomeBuddy page."""

    def test_contractor_not_found_flow(self, browser):
        """Test the HomeBuddy page."""
        hvac_page = HvacPage(browser)
        hvac_page.fill_input("10001", "zipCode", "zipCode")
        hvac_page.click_on_button(HvacPage.button("Get estimate"))

        hvac_page.click_on_button(HvacPage.tile_button("Repair"))
        hvac_page.check_message(hvac_page.repair_message_text)
        hvac_page.click_on_button(HvacPage.button("Yes"))

        hvac_page.click_on_button(HvacPage.tile_button("Air conditioner"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Less than 5 "))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Detached"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.fill_input("300", "squareFeet", "squareFeet")
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Yes"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.fill_input("Sam Smith", "fullName", "fullName")
        hvac_page.fill_input("test@email.com", "email", "email")
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.fill_input("12345678901", "phoneNumber", "phoneNumber")
        hvac_page.click_on_button(HvacPage.button("Submit my request"))

        hvac_page.check_message(hvac_page.searching_message, to_disappear=True)
        hvac_page.click_on_button(HvacPage.button("Go to homepage"))
        assert_equal("https://hb-autotests.stage.sirenltd.dev/", browser.current_url, "URL is not correct")

    def test_get_contractor_flow_wrong_name_email(self, browser):
        """Test the HomeBuddy page."""
        hvac_page = HvacPage(browser)
        hvac_page.fill_input("10001", "zipCode", "zipCode")
        hvac_page.click_on_button(HvacPage.button("Get estimate"))

        hvac_page.click_on_button(HvacPage.tile_button("Replacement"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Water heater"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Propane"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("5 to 10"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Detached"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.checkbox("Not sure"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.click_on_button(HvacPage.tile_button("Yes"))
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.fill_input("BrandonFaircloth", "fullName", "fullName")
        hvac_page.fill_input("testemail.com", "email", "email")
        hvac_page.click_on_button(HvacPage.button("Next"))

        hvac_page.check_field_validation_message('Full name must be written in English letters and dashes if needed.',
                                                 "fullName")
        hvac_page.check_field_validation_message("Must be a valid email address.", "email")
