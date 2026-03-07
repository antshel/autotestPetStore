import requests
from endpoint.base_endpoints import Endpoints

class CreatePet(Endpoints):

    def new_pet(self, payload):
        self.response = requests.post(f'https://petstore.swagger.io/v2/pet', json=payload)
        self.response_json = self.response.json()

    def check_id_in_response(self, id):
        assert self.response_json['id'] == id

   

