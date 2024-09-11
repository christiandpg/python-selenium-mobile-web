import pytest
from selenium import webdriver
from config.config import BASE_URL
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope='function')
def driver(request):
    chrome_options = Options()
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(BASE_URL)

    def teardown():
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = f"screenshots/screenshot_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()

    request.addfinalizer(teardown)
    return driver