from helpers.selenium_helpers import SeleniumHelpers


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelpers(driver)
        self.channel_tab_css = "ul > li:nth-child(2) > a[role='tab']"
        self.channels_css = "div[class^=Layout-sc] > div[class^=Layout-sc] img.tw-image"

    def go_to_channels_tab_and_scroll(self, scroll_count):
        channels_tab = self.helper.wait_for_element_clickable_by_css(self.channel_tab_css)
        channels_tab.click()
        self.helper.wait_url_contains('type=channels')
        self.scroll_down_search_results(scroll_count)

    def click_on_random_channel(self):
        channel_img = self.helper.wait_for_all_elements_by_css(self.channels_css)
        count = len(channel_img)
        channel_img[count-1].click()

    def scroll_down_search_results(self, scroll_count):
        self.helper.scroll_web_page(scroll_count)

    def url_contains(substring):
        def _url_contains(driver):
            return substring in driver.current_url

        return _url_contains
