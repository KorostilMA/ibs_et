from reqres_framework.ui_framework import BaseUi


class TestRegisterSuccessful(BaseUi):
    button_label = ' Register - successful '
    resource_name = 'register'


class TestLoginSuccessful(BaseUi):
    button_label = ' Login - successful '
    resource_name = 'login'


class TestGetUserList(BaseUi):
    button_label = ' List users '
    resource_name = 'users'
