from reqres_framework.api_framework import RESTResource


class TestUsersResource(RESTResource):
    resource_name = 'users'
    resource_fields = {'id', 'email', 'first_name', 'last_name', 'avatar'}
    existent_resource_id = 2
    non_existent_resource_id = 23


class TestUnknownResource(RESTResource):
    resource_name = 'unknown'
    resource_fields = {'id', 'name', 'year', 'color', 'pantone_value'}
    existent_resource_id = 2
    non_existent_resource_id = 23
