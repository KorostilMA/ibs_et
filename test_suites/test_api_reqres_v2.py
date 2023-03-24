from test_suites.test_api_reqres_v1 import TestUsersResource, TestUnknownResource


class TestUsersResourceV2(TestUsersResource):
    def test_get_single(self):
        print('V2')


class TestUnknownResourceV2(TestUnknownResource):
    pass
