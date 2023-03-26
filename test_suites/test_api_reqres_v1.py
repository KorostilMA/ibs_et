"""Тестирование конкретных ресурсов раздела Give It A Try сайта reqres"""
from http import HTTPStatus
import requests
from reqres_framework.api_framework import RESTResource


class TestUsersResource(RESTResource):
    """Тестирование ресурса users CRUD"""

    resource_name = 'users'
    resource_fields = {'id', 'email', 'first_name', 'last_name', 'avatar'}
    existent_resource_id = 2
    non_existent_resource_id = 23
    create_resource_data = {'name': 'morpheus', 'job': 'leader'}
    update_resource_data = {'name': 'morpheus', 'job': 'zion resident'}


class TestUnknownResource(RESTResource):
    """Тестирование ресурса unknown CRUD"""

    resource_name = 'unknown'
    resource_fields = {'id', 'name', 'year', 'color', 'pantone_value'}
    existent_resource_id = 2
    non_existent_resource_id = 23
    create_resource_data = {'name': 'fuchsia rose', 'year': '2001',
                            'color': '#C74375', 'pantone_value': '17-2031'}
    update_resource_data = {'name': 'fuchsia updated', 'year': '2005',
                            'color': '#C74375', 'pantone_value': '17-2031'}


def test_login_successful(base_url):
    """Проверяем авторизацию"""

    url = f'{base_url}/api/login'
    response = requests.post(url=url, data={'email': 'eve.holt@reqres.in','password': 'cityslicka'})

    assert response.status_code == HTTPStatus.OK
    assert 'token' in response.json()


def test_login_unsuccessful(base_url):
    """Проверяем авторизацию"""

    url = f'{base_url}/api/login'
    response = requests.post(url=url, data={'email': 'eve.holt@reqres.in'})

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'error': 'Missing password'}


def test_register_successful(base_url):
    """Проверяем регистрацию"""

    url = f'{base_url}/api/register'
    response = requests.post(url=url, data={'email': 'eve.holt@reqres.in', 'password': 'pistol'})

    assert response.status_code == HTTPStatus.OK
    json_response = response.json()
    assert 'token' in json_response
    assert 'id' in json_response


def test_register_unsuccessful(base_url):
    """Проверяем регистрацию"""

    url = f'{base_url}/api/register'
    response = requests.post(url=url, data={'email': 'sydney@fife'})

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'error': 'Missing password'}
