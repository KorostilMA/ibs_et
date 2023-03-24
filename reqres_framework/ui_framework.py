import pytest
import brotli
import json
import time
from locators_for_ui.common_objects import ResponseSection, RequestSendingSection


class BaseUi:
    driver = None
    button_label = None
    resource_name = None

    @pytest.fixture(scope='module')
    def driver(self, browser_driver, base_url):
        url = f'{base_url}/api/{self.resource_name}'
        browser_driver.scopes = [f'.*{url}*']
        browser_driver.get(base_url)
        return browser_driver

    @pytest.fixture
    def send_request_by_button_click(self, driver):
        reg_page = RequestSendingSection(driver)
        reg_page.send_request(button_label=self.button_label)
        time.sleep(10)  # сделать умнее, не успела

    @pytest.fixture
    def get_response_from_ui(self, driver, send_request_by_button_click):
        common = ResponseSection(driver)
        code_str = common.get_code_from_field()
        output_str = common.get_output_from_field()
        return code_str, output_str

    @pytest.fixture
    def get_response_from_network(self, driver, send_request_by_button_click):
        request_from_network = driver.requests[-1]
        response = request_from_network.response
        if response.headers.get('content-encoding') == 'br':
            response.body = brotli.decompress(response.body)
        return response

    def test_response_sameness(self, get_response_from_ui, get_response_from_network):
        assert get_response_from_network.status_code == (int(get_response_from_ui[0]))
        assert json.loads(get_response_from_network.body) == json.loads(get_response_from_ui[1])
