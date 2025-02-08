from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class FinishPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button_xpath_two = Locators.cart_button_xpath_two
        self.contact_dropdown_xpath = Locators.contact_dropdown_xpath
        self.contact_option_xpath = Locators.contact_option_xpath
        self.next_button_1_xpath = Locators.next_button_1_xpath
        self.billing_dropdown_xpath = Locators.billing_dropdown_xpath
        self.billing_option_fernando_xpath = Locators.billing_option_fernando_xpath

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button_xpath_two))
        ).click()

    def select_contact(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_dropdown_xpath))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.contact_option_xpath))
        ).click()

    def click_next_after_contact(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.next_button_1_xpath))
        ).click()

    def select_billing(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.billing_dropdown_xpath))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.billing_option_fernando_xpath))
        ).click()
