from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

from Locators.locators import Locators
from Pages.loginPage import LoginPage
import HtmlTestRunner

class LoginTet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://dev.market.orion.global/es/store/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        login = LoginPage(self.driver)
        login.click_login_page()
        login.enter_username('fojedaleonardo@gmail.com')
        login.enter_password('ROMAD2020')
        login.click_login()

        expected_url = 'https://dev.market.orion.global/es/store/'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        self.assertEqual(self.driver.current_url, expected_url)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
