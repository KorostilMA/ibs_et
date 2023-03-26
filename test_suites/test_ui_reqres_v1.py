"""UI-Тесты для каждой кнопки из раздела Give It A Try"""
from reqres_framework.ui_framework import BaseUi


class TestGetUserList(BaseUi):
    button_id = 'users'
    resource_name = 'users'


class TestGetSingleUser(BaseUi):
    button_id = 'users-single'
    resource_name = 'users'


class TestSingleUserNotFound(BaseUi):
    button_id = 'users-single-not-found'
    resource_name = 'users'


class TestGetListResource(BaseUi):
    button_id = 'unknown'
    resource_name = 'unknown'


class TestGetSingleResource(BaseUi):
    button_id = 'unknown-single'
    resource_name = 'unknown'


class TestGetSingleResourceNotFound(BaseUi):
    button_id = 'unknown-single-not-found'
    resource_name = 'unknown'


class TestCreateUser(BaseUi):
    button_id = 'post'
    resource_name = 'users'


class TestUpdatePutUser(BaseUi):
    button_id = 'put'
    resource_name = 'users'


class TestUpdatePatchUser(BaseUi):
    button_id = 'patch'
    resource_name = 'users'


class TestDeleteUser(BaseUi):
    button_id = 'delete'
    resource_name = 'users'


class TestRegisterSuccessful(BaseUi):
    button_id = 'register-successful'
    resource_name = 'register'


class TestRegisterUnSuccessful(BaseUi):
    button_id = 'register-unsuccessful'
    resource_name = 'register'


class TestLoginSuccessful(BaseUi):
    button_id = 'login-successful'
    resource_name = 'login'


class TestLoginUnSuccessful(BaseUi):
    button_id = 'login-unsuccessful'
    resource_name = 'login'


class TestDelayedResponse(BaseUi):
    button_id = 'delay'
    resource_name = 'users'
