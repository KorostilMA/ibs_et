"""Базовый UI-тест"""
import json
import time

import brotli
import pytest

from locators_for_ui.common_objects import ResponseSection, RequestSendingSection


class BaseUi:
    driver = None
    button_id = None
    resource_name = None

    @pytest.fixture(scope='module')
    def driver(self, browser_driver, base_url):
        """Задаём для seleniumwire диапозон отслеживаемых запросов в network
        Открываем страницу сайта из конфига"""

        url = f'{base_url}/api/{self.resource_name}'
        browser_driver.scopes = [f'.*{url}*']
        browser_driver.get(base_url)
        return browser_driver

    @pytest.fixture
    def send_request_by_button_click(self, driver):
        """Жмём на конпку интересующего запроса"""

        reg_page = RequestSendingSection(driver)
        reg_page.send_request(button_id=self.button_id)
        time.sleep(1)
        reg_page.wait_for_spinner_tobe_hidden()

    @pytest.fixture
    def get_response_from_ui(self, driver, send_request_by_button_click):
        """Берём из разметки страницы ответ запроса"""

        common = ResponseSection(driver)
        code_str = common.get_code_from_field()
        output_str = common.get_output_from_field()
        return code_str, output_str

    @pytest.fixture
    def get_response_from_network(self, driver, send_request_by_button_click):
        """Берём ответ запроса из Network, помогает нам selenium-wire"""

        request_from_network = driver.requests[-1]
        response = request_from_network.response
        if response.headers.get('content-encoding') == 'br':
            response.body = brotli.decompress(response.body)
        return response

    @staticmethod
    def test_response_sameness(get_response_from_ui, get_response_from_network):
        """Сравниваем данные, которые получили из сети, с теми,
        что отобразились на странице"""

        try:
            json_body_from_ui = json.loads(get_response_from_ui[1])
        except json.decoder.JSONDecodeError:
            json_body_from_ui = ''

        try:
            json_body_from_network = json.loads(get_response_from_network.body)
        except json.decoder.JSONDecodeError:
            json_body_from_network = ''

        assert get_response_from_network.status_code == int(get_response_from_ui[0])
        assert json_body_from_network == json_body_from_ui
