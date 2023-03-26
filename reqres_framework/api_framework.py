import pytest
import requests
from http import HTTPStatus


class RESTResource:
    resource_name = None
    resource_fields = None
    existent_resource_id = None
    non_existent_resource_id = None
    create_resource_data = None
    update_resource_data = None

    @pytest.fixture(autouse=True)
    def setup(self, base_url):
        self.url = f'{base_url}/api/{self.resource_name}'

    @pytest.mark.parametrize('page', ['a', 0])
    def test_invalid_page(self, page):
        response = requests.get(self.url, params={'page': page})
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_get_list(self):
        response = requests.get(self.url)

        assert response.status_code == HTTPStatus.OK
        json_response = response.json()
        assert json_response['page'] > 0
        assert json_response['per_page'] > 0
        assert json_response['total'] >= 0
        assert json_response['total_pages'] >= 0
        if json_response['total'] > json_response['per_page']:
            assert len(json_response['data']) == json_response['per_page']
        assert set(json_response['data'][0].keys()) == self.resource_fields

    def test_get_single(self):
        response = requests.get(f'{self.url}/{self.existent_resource_id}')

        assert response.status_code == HTTPStatus.OK
        json_response = response.json()
        assert json_response['data']['id'] == self.existent_resource_id
        assert set(json_response['data']) == self.resource_fields

    def test_get_single_not_found(self):
        response = requests.get(f'{self.url}/{self.non_existent_resource_id}')
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_create(self):
        response = requests.post(self.url, data=self.create_resource_data)

        assert response.status_code == HTTPStatus.CREATED
        assert self.create_resource_data.items() <= response.json().items()

    def test_put_update(self):
        response = requests.put(f'{self.url}/{self.existent_resource_id}', data=self.update_resource_data)

        assert response.status_code == HTTPStatus.OK
        assert self.update_resource_data.items() <= response.json().items()

    def test_put_update_not_found(self):
        response = requests.put(f'{self.url}/{self.non_existent_resource_id}')
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_patch_update(self):
        response = requests.patch(f'{self.url}/{self.existent_resource_id}', data=self.update_resource_data)

        assert response.status_code == HTTPStatus.OK
        assert self.update_resource_data.items() <= response.json().items()
    def test_patch_update_not_found(self):
        response = requests.patch(f'{self.url}/{self.non_existent_resource_id}')
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_delete(self):
        response = requests.delete(f'{self.url}/{self.existent_resource_id}')
        assert response.status_code == HTTPStatus.NO_CONTENT

    def test_delete_not_found(self):
        response = requests.delete(f'{self.url}/{self.non_existent_resource_id}')
        assert response.status_code == HTTPStatus.NOT_FOUND
