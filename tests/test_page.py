from pages.hvac_page import HvacPage


class TestHomeBuddyPage:
    """Tests for the HomeBuddy page."""

    def test_homebuddy_page(self, browser):
        """Test the HomeBuddy page."""
        hvac_page = HvacPage(browser)
        hvac_page.fill_zip_code("10001")
        hvac_page.click_on_button(HvacPage.page_button("Get estimate"))
        hvac_page.click_on_button(hvac_page.repair_button)
        hvac_page.check_message(hvac_page.repair_message_text)
        hvac_page.click_on_button(HvacPage.page_button("No"))
        hvac_page.check_message(hvac_page.sorry_message_text)
        hvac_page.click_on_button(HvacPage.page_button("Go to homepage"))
