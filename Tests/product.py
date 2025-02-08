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
        # Configuración inicial del navegador
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://dev.market.orion.global/es/store/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_add_two_products_to_cart(self):
        # **Inicio de sesión**
        login_page = LoginPage(self.driver)
        login_page.click_login_page()
        login_page.enter_username('cuentademoorionhub@gmail.com')
        login_page.enter_password("12345678Fs")
        login_page.click_login()
        login_page.validate_login_successful()

        # **Agregar productos al carrito**
        product_page = ProductPage(self.driver)

        # Producto 1
        product_name_1 = "Tooglebox Premium"
        product_page.search_and_submit(product_name_1)
        time.sleep(2)
        product_page.open_options_menu()
        product_page.select_add_licenses()
        product_page.set_quantity_and_confirm()
        product_page.add_to_cart()
        product_page.continue_shopping()

        # Producto 2
        product_name_2 = "Gemini Enterprise"
        product_page.search_and_submit(product_name_2)
        time.sleep(2)
        product_page.open_options_menu()
        product_page.select_add_licenses()
        product_page.set_quantity_and_confirm()
        product_page.add_to_cart()
        product_page.continue_shopping()

        # **Navegar al carrito**
        self.driver.find_element(By.XPATH, Locators.go_to_cart_button_xpath).click()

        # **Validar productos en el carrito**
        cart_product_names = self.driver.find_elements(By.XPATH, Locators.cart_product_names_xpath)
        cart_product_prices = self.driver.find_elements(By.XPATH, Locators.cart_product_prices_xpath)
        cart_total_price = self.driver.find_element(By.XPATH, Locators.cart_total_price_xpath).text

        # Extraer nombres y precios
        product_names = [name.text for name in cart_product_names]
        product_prices = [float(price.text.replace("$", "").replace(",", "").strip()) for price in cart_product_prices]
        total_price_calculated = sum(product_prices)

        # Validar nombres de los productos
        self.assertIn(product_name_1, product_names, "Producto 1 no está en el carrito.")
        self.assertIn(product_name_2, product_names, "Producto 2 no está en el carrito.")

        # Validar precio total
        self.assertEqual(total_price_calculated, float(cart_total_price.replace("$", "").replace(",", "").strip()),
                         "El precio total en el carrito no coincide con la suma de los productos.")

        print("Productos agregados y validados correctamente.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()
