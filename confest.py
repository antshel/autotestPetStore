import pytest
from endpoint.create_pet import CreatePet
from endpoint.delete_pet import DeletePet

@pytest.fixture()
def obj_id():
    create_pet_endpoints = CreatePet()
    delete_pet_endpoints = DeletePet()
    payload = {
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Barbos",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
    create_pet_endpoints.new_pet(payload)
    yield create_pet_endpoints.response_json['id']
    delete_pet_endpoints.delete_pet_by_id(create_pet_endpoints.response_json['id'])
 
