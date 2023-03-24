"""Методы и локаторы страницы https://reqres.in/"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ResponseSection:

    def __init__(self, driver):
        self.driver = driver
        self.response_code_fld = driver.find_element(By.CSS_SELECTOR, '.response-code')
        self.response_output_fld = driver.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')

    def get_code_from_field(self):

        return self.response_code_fld.text

    def get_output_from_field(self):

        return self.response_output_fld.text


class RequestSendingSection:

    def __init__(self, driver=None):
        self.driver = driver
        self.successful_register_btn = driver.find_element(By.CSS_SELECTOR, '[data-id="register-successful"]')
        self.unsuccessful_register_btn = driver.find_element(By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')

    def send_request(self, button_label):

        button = self.driver.find_element(By.XPATH, f"//*[.='{button_label}']")
        ActionChains(self.driver).move_to_element(button).perform()
        button.click()






