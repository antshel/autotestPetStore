import requests
from endpoint.base_endpoints import Endpoints

class DeletePet(Endpoints):

    def delete_pet_by_id(self, pet_id):
        self.response = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}')
        try:
            self.response_json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.response_json = None
        return self.response
