# 🧪 Test Automation - Mobile Web - Python, Pytest, Selenium
The purpose of this project is to implement an automated test using python. The test will open the browser emulating a 
mobile device, go to Twitch website, search for a streamer and wait until the video loads. 
At the end a screenshot is saved at `screenshots` folder.

## 🛠️ Prerequisites
Ensure you have the following installed before running the project:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Poetry**: [Poetry Installation Guide](https://python-poetry.org/docs/#installation)
- **Web browser driver** for Selenium (e.g., ChromeDriver)

## 🚀 Setup
1. Clone the repository:
``````
git clone https://github.com/christiandpg/python-selenium-mobile-web.git
cd python-selenium-mobile-web
``````

2. Install dependencies using Poetry:
```poetry install```


## 🗂️ PROJECT STRUCTURE
<pre>
project-root
│
├── config
│   └── config.py                   # test data - URL, search strings
│
├── fixtures
│   └── setup.py                    # webdriver configuration / teardown 
│
├── helpers
│   └── selenium_helpers.py         # webDriverWait methods

├── screenshots
│   └── screenshot.png              # saved screenshots
│
├── pages
│   ├── home_page.py                # home page object
│   ├── search_page.py              # search page object
│   ├── search_results_page.py      # search results page object
│   └── streamer_page.py            # streamer page object
│
├── tests
│   └── test_select_streamer.py     # main test scenario
│
</pre>

## 🏃Running Tests
 Execute the following command in your Terminal:
```pytest```


![GIF](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG9paWpxaG04bHhpaG11d3h4Z3MybmIzaHN3dngwN2NqbzU1ZTVsbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/meYIaKNGVvjnVXJetK/giphy.gif)
## 🧑‍💻 IDE Integration
This project is configured to work seamlessly with PyCharm. Make sure to set up your IDE following the project's configurations.
