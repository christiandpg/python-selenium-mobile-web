from helpers.selenium_helpers import SeleniumHelpers


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelpers(driver)
        self.search_icon_css = "a[aria-label='Search']"
        self.main_content_wrapper_id = "page-main-content-wrapper"

    def is_main_wrapper_displayed(self):
        try:
            main_wrapper = self.helper.wait_for_element_by_id(self.main_content_wrapper_id)
            return main_wrapper.is_displayed()
        except Exception:
            return False

    def click_on_search_button(self):
        search_icon = self.helper.wait_for_element_clickable_by_css(self.search_icon_css)
        search_icon.click()