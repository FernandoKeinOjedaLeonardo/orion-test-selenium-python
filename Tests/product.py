import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Pages.productPage import ProductPage
from Pages.loginPage import LoginPage
from Locators.locators import Locators

class ProductTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://dev.market.orion.global/es/store/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_add_two_products_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.click_login_page()
        login_page.enter_username('cuentademoorionhub@gmail.com')
        login_page.enter_password("12345678Fs")
        login_page.click_login()
        login_page.validate_login_successful()

        product_page = ProductPage(self.driver)

        # Agregar primer producto
        product_name_1 = "Google Workspace Enterprise Standard"
        product_page.search_and_submit(product_name_1)
        time.sleep(2)
        product_page.open_options_menu()
        product_page.select_add_licenses()
        product_page.set_quantity_and_confirm()
        product_page.add_to_cart()
        product_page.continue_shopping()

        # Agregar segundo producto
        product_name_2 = "Gemini Enterprise"
        product_page.search_and_submit(product_name_2)
        time.sleep(2)
        product_page.open_options_menu()
        product_page.select_add_licenses()
        product_page.set_quantity_and_confirm()
        product_page.add_to_cart()
        product_page.continue_shopping()

        # Ir al carrito
        self.driver.find_element(By.XPATH, Locators.go_to_cart_button_xpath).click()

        # Obtener nombre y precio del primer producto
        product_name_cart_1 = self.driver.find_element(By.XPATH, Locators.cart_product_names_xpath).text
        product_price_cart_1 = float(
            self.driver.find_element(By.XPATH, Locators.cart_product_prices_xpath).text.replace("$", "").replace(",", ".").strip()
        )

        # Obtener nombre y precio del segundo producto
        product_name_cart_2 = self.driver.find_element(By.XPATH, Locators.cart_product_names_two_xpath).text
        product_price_cart_2 = float(
            self.driver.find_element(By.XPATH, Locators.cart_product_prices_two_xpath).text.replace("$", "").replace(",", ".").strip()
        )

        # Validar nombres de productos
        self.assertEqual(product_name_1, product_name_cart_1, "El primer producto no coincide en el carrito.")
        self.assertEqual(product_name_2, product_name_cart_2, "El segundo producto no coincide en el carrito.")

        # Validar precios y total
        cart_total_price = float(
            self.driver.find_element(By.XPATH, Locators.cart_total_price_xpath).text.replace("$", "").replace(",", ".").strip()
        )

        calculated_total_price = product_price_cart_1 + product_price_cart_2

        self.assertEqual(
            calculated_total_price,
            cart_total_price,
            msg="El precio total en el carrito no coincide con la suma de los productos."
        )
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")