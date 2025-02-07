from selenium.webdriver.common.by import By
from Locators.locators import Locators
class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.opcion_page_xpath = Locators.opcion_page_xpath
        self.opcion_product_xpath = Locators.opcion_product_xpath
        self.opcion_buy_xpath = Locators.opcion_buy_xpath

    def click_search(self):
        self.driver.find_element(By.XPATH, self.opcion_page_xpath).click()

    def click_select_product(self):
        self.driver.find_element(By.XPATH, self.opcion_product_xpath).click()

    def click_select_buy(self):
        self.driver.find_element(By.XPATH, self.opcion_buy_xpath).click()