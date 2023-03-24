import json
import pytest
from pathlib import Path
from seleniumwire import webdriver
from seleniumwire.webdriver import ChromeOptions


CONFIG_PATH = Path('config.json')
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def base_url(config):
    return config['start_url']


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):

    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def browser_driver(config_browser, config_wait_time):
    if config_browser == 'chrome':
        chrome_options = ChromeOptions()  #
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()
