from selenium.webdriver.common.by import By
from Locators.locators import Locators
class SearchPage():

    def __init__(self, driver):
        self.driver = driver
        self.opcion_page_xpath = Locators.opcion_page_xpath

    def click_search(self):
        self.driver.find_element(By.XPATH, self.opcion_page_xpath).click()