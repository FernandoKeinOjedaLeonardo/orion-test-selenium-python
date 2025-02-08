from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.three_dots_button_xpath = Locators.three_dots_button_xpath
        self.add_licenses_option_xpath = Locators.add_licenses_option_xpath
        self.increase_quantity_button_xpath = Locators.increase_quantity_button_xpath
        self.no_option_xpath = Locators.no_option_xpath
        self.add_to_cart_button_xpath = Locators.add_to_cart_button_xpath
        self.continue_shopping_button_xpath = Locators.continue_shopping_button_xpath
        self.search_box_xpath = Locators.search_box_xpath

    def search_and_submit(self, product_name):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_box.clear()
        search_box.send_keys(product_name + "\n")  # Presiona Enter para buscar

    def open_options_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.three_dots_button_xpath))
        ).click()

    def select_add_licenses(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_licenses_option_xpath))
        ).click()

    def set_quantity_and_confirm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.increase_quantity_button_xpath))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.no_option_xpath))
        ).click()

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_xpath))
        ).click()

    def continue_shopping(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_shopping_button_xpath))
        ).click()
