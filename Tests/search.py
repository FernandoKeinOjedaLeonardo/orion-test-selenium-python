import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage
from Pages.searchPage import SearchPage

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuración inicial del navegador
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://dev.market.orion.global/es/store/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_and_search_product(self):
        login_page = LoginPage(self.driver)
        login_page.click_login_page()
        login_page.enter_username("cuentademoorionhub@gmail.com")
        login_page.enter_password("12345678Fs")
        login_page.click_login()
        login_page.validate_login_successful()

        search_page = SearchPage(self.driver)
        search_term = "Google"
        search_page.enter_search_term_and_submit(search_term)
        time.sleep(1)
        search_page.validate_results_present()
        time.sleep(2)
        search_page.capture_first_product()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")