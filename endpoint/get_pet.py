import requests
from endpoint.base_endpoints import Endpoints

class GetPet(Endpoints):

    def get_pet_by_id(self, pet_id):
        self.response = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}')
        self.response_json = self.response.json()
    def get_by_status(self, status):
        self.response = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}')
        self.response_json = self.response.json()
    def check_response_id(self, id):
        assert self.response_json['id'] == id


