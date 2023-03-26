"""Методы и локаторы страницы https://reqres.in/ пробуем жить по канонам pageObject Model  """

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ResponseSection:
    """Раздел Give it a try - демонстрация ответа на запрос"""

    def __init__(self, driver):
        self.driver = driver
        self.response_code_fld = driver.find_element(By.CSS_SELECTOR, '.response-code')
        self.response_output_fld = driver.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')

    def get_code_from_field(self):
        """Взять код ответа"""

        return self.response_code_fld.text

    def get_output_from_field(self):
        """Взять тело ответа"""

        return self.response_output_fld.text


class RequestSendingSection:
    """Раздел Give it a try - отправка запроса"""

    def __init__(self, driver=None):
        self.driver = driver
        self.successful_register_btn = driver.find_element(By.CSS_SELECTOR, '[data-id="register-successful"]')
        self.unsuccessful_register_btn = driver.find_element(By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
        self.spinner_has_stopped = driver.find_element(By.CSS_SELECTOR, '.spinner[hidden="true"]')

    def wait_for_spinner_tobe_hidden(self):
        """Ждём, когда пропадёт спиннер загрузки ответа"""

        sp_locator = '.spinner[hidden="true"]'
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sp_locator)))

    def send_request(self, button_id):
        """Отправляем запрос через клик по соответствующей кнопке"""

        button = self.driver.find_element(By.CSS_SELECTOR, f'[data-id="{button_id}"]')
        ActionChains(self.driver).move_to_element(button).perform()
        button.click()






