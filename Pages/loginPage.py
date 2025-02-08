from selenium.webdriver.support import expected_conditions as EC

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.password_textbox_xpath = Locators.password_textbox_xpath
        self.login_button_xpath = Locators.login_button_xpath
        self.login_page_xpath = Locators.login_page_xpath
        self.login_success_element_xpath  = Locators.login_success_element_xpath

    def click_login_page(self):
        self.driver.find_element(By.XPATH, self.login_page_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def validate_login_successful(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.login_success_element_xpath))
        )

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
