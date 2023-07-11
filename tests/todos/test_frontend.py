from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TodosFrontendTestCase(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("disable-extensions")
        self.selenium = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        super(TodosFrontendTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TodosFrontendTestCase, self).tearDown()

    def test_register(self):
        self.selenium.get('http://127.0.0.1:8000/')