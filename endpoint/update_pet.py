import requests
from endpoint.base_endpoints import Endpoints

class UpdatePet(Endpoints):

    def update_pet_by_id(self, payload):
        self.response = requests.put(f'https://petstore.swagger.io/v2/pet/', json=payload)
        self.response_json = self.response.json()
