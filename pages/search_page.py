from helpers.selenium_helpers import SeleniumHelpers


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelpers(driver)
        self.search_input_css = "input[data-a-target='tw-input']"
        self.search_result_items_css = "div[class^=Layout-sc] > ul > li > a p"

    def perform_search(self, search_text):
        search_input = self.helper.wait_for_element_clickable_by_css(self.search_input_css)
        search_input.send_keys(search_text)
        self.click_result_in_the_list()

    def click_result_in_the_list(self):
        search_result_items = self.helper.wait_for_element_clickable_by_css(self.search_result_items_css)
        search_result_items.click()