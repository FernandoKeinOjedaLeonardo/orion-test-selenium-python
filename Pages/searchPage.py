from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box_xpath = Locators.search_box_xpath
        self.product_name_xpath = Locators.product_name_xpath
        self.product_price_xpath = Locators.product_price_xpath

    def enter_search_term_and_submit(self, term):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_box.clear()
        search_box.send_keys(term)
        search_box.send_keys(Keys.ENTER)

    def validate_results_present(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.product_name_xpath))
        )

    def capture_first_product(self):
        product_name = self.driver.find_element(By.XPATH, self.product_name_xpath).text
        product_price = self.driver.find_element(By.XPATH, self.product_price_xpath).text
        print(f"Primer producto encontrado: {product_name} - Precio: {product_price}")
