"""UI-Тесты для каждой кнопки из раздела Give It A Try"""
from reqres_framework.ui_framework import BaseUi


class TestGetUserList(BaseUi):
    button_label = ' List users '
    resource_name = 'users'


class TestGetSingleUser(BaseUi):
    button_label = ' Single user '
    resource_name = 'users'


class TestSingleUserNotFound(BaseUi):
    button_label = ' Single user not found '
    resource_name = 'users'


class TestGetListResource(BaseUi):
    button_label = ' List <resource> '
    resource_name = 'unknown'


class TestGetSingleResource(BaseUi):
    button_label = ' Single <resource> '
    resource_name = 'unknown'


class TestDeleteUser(BaseUi):
    button_label = ' Delete '
    resource_name = 'users'


class TestRegisterSuccessful(BaseUi):
    button_label = ' Register - successful '
    resource_name = 'register'


class TestRegisterUnSuccessful(BaseUi):
    button_label = ' Register - unsuccessful '
    resource_name = 'register'


class TestLoginSuccessful(BaseUi):
    button_label = ' Login - successful '
    resource_name = 'login'


class TestLoginUnSuccessful(BaseUi):
    button_label = ' Login - unsuccessful '
    resource_name = 'login'


class TestCreateUser(BaseUi):
    button_label = ' Create '
    resource_name = 'users'


class TestDelayedResponse(BaseUi):
    button_label = ' Delayed response '
    resource_name = 'users'
