from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.search_results_page import SearchResultPage
from pages.streamer_page import StreamerPage
from fixtures.setup import driver
from config.config import SEARCH_STRING


def test_streamer_search(driver):
    home_page = HomePage(driver)
    home_page.is_main_wrapper_displayed()
    home_page.click_on_search_button()

    search_page = SearchPage(driver)
    search_page.perform_search(SEARCH_STRING)

    search_results_page = SearchResultPage(driver)
    search_results_page.go_to_channels_tab_and_scroll(2)
    search_results_page.click_on_random_channel()

    streamer_page = StreamerPage(driver)
    streamer_page.wait_until_player_controls_displayed()
    assert streamer_page.are_all_elements_displayed(), "One or more elements are not displayed"
