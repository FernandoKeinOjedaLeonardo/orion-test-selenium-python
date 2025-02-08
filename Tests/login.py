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
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        login = LoginPage(self.driver)
        login.click_login_page()
        login.enter_username('cuentademoorionhub@gmail.com')
        login.enter_password('12345678Fs')
        login.click_login()

        login.validate_login_successful()
        self.assertTrue(
            self.driver.find_element(By.XPATH, login.login_success_element_xpath).is_displayed(),
            "El elemento de éxito no está presente después del login."
        )
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
