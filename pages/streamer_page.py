from helpers.selenium_helpers import SeleniumHelpers


class StreamerPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = SeleniumHelpers(driver)
        self.video_player_css = "[data-test-selector='video-player__video-container']"
        self.streamer_avatar_css = "div[class^=ScAvatar] > img"
        self.follow_button_css = "button[data-a-target='follow-button']"
        self.dropdown_menu_css = "button[aria-label='Open Dropdown Menu']"
        self.chat_container_css = "div[aria-label='Chat messages']"
        self.chat_line_message_css = "div.chat-line__message"
        self.open_app_to_chat_css = "button[class^=ScInteractableBase-sc] p"
        self.player_controls_css = "div[data-a-target='player-controls'][data-a-visible=true]"

    def is_video_player_displayed(self):
        try:
            video_player = self.helper.wait_for_element_by_css(self.video_player_css)
            return video_player.is_displayed()
        except Exception:
            return False

    def is_follow_button_displayed(self):
        try:
            follow_button = self.helper.wait_for_element_by_css(self.follow_button_css)
            return follow_button.is_displayed()
        except Exception:
            return False

    def is_dropdown_menu_displayed(self):
        try:
            dropdown_menu = self.helper.wait_for_element_by_css(self.dropdown_menu_css)
            return dropdown_menu.is_displayed()
        except Exception:
            return False

    def is_chat_container_displayed(self):
        try:
            chat_container = self.helper.wait_for_element_by_css(self.chat_container_css)
            return chat_container.is_displayed()
        except Exception:
            return False

    def wait_until_player_controls_displayed(self):
        try:
            player_controls = self.helper.wait_for_element_by_css(self.player_controls_css, 30)
            return player_controls.is_displayed()
        except Exception:
            return False

    def is_open_app_to_chat_displayed(self):
        try:
            open_app_to_chat = self.helper.wait_for_element_by_css(self.open_app_to_chat_css)
            return open_app_to_chat.is_displayed()
        except Exception:
            return False

    def are_all_elements_displayed(self):
        return (self.is_video_player_displayed()
                and self.is_follow_button_displayed()
                and self.is_dropdown_menu_displayed()
                and self.is_chat_container_displayed()
                and self.is_open_app_to_chat_displayed())