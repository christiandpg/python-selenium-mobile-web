from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_by_id(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))

    def wait_for_element_by_css(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_id)))

    def wait_for_element_clickable_by_id(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.ID, element_id)))

    def wait_for_element_clickable_by_css(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_id)))

    def wait_for_all_elements_by_css(self, element_id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, element_id)))

    def wait_url_contains(self, text):
        return WebDriverWait(self.driver, 10).until(lambda d: text in d.current_url)

    def scroll_web_page(self, scroll_count):
        for _ in range(scroll_count):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")