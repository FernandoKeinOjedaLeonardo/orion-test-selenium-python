import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.finishPage import FinishPage
from Pages.loginPage import LoginPage


class FinishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://dev.market.orion.global/es/store/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_complete_purchase(self):
        login_page = LoginPage(self.driver)
        login_page.click_login_page()
        login_page.enter_username('cuentademoorionhub@gmail.com')
        login_page.enter_password("12345678Fs")
        login_page.click_login()
        login_page.validate_login_successful()
        finish_page = FinishPage(self.driver)

        finish_page.go_to_cart()
        finish_page.select_contact()
        finish_page.click_next_after_contact()
        finish_page.select_billing()

        print("Flujo completado correctamente hasta la selección de la razón social.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test finalizado correctamente.")
