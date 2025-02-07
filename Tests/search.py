import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Locators.locators import Locators
from Pages.searchPage import SearchPage

class SearchTet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://dev.market.orion.global/es/store/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_valid(self):
        search = SearchPage(self.driver)
        search.click_search()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

