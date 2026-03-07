import pytest
import requests
from endpoint.create_pet import CreatePet
from endpoint.delete_pet import DeletePet
from endpoint.get_pet import GetPet
from endpoint.update_pet import UpdatePet
from tests.test_data import payloads
from confest import obj_id



@pytest.mark.parametrize('payload', payloads.payload)
def test_create_pet_success(payload):
    create_pet_endpoint = CreatePet()
    create_pet_endpoint.new_pet(payload)
    create_pet_endpoint.check_status_in_response(payload['status'])
    create_pet_endpoint.chek_name_pet_in_response(payload['name'])
    create_pet_endpoint.status_code_is_200()


def test_create_invalid_id_type():
    create_pet_endpoint = CreatePet()
    create_pet_endpoint.new_pet({"id": "invalid_id"})
    create_pet_endpoint.status_code_is_500()

def test_empty_body():
    create_pet_endpoint = CreatePet()
    create_pet_endpoint.new_pet({})
    create_pet_endpoint.status_code_is_405()

@pytest.mark.parametrize('payload_without_name', payloads.payload_without_name)
def test_create_without_name(payload_without_name):
    create_pet_endpoint = CreatePet()
    create_pet_endpoint.new_pet(payload_without_name)
    create_pet_endpoint.status_code_is_405()

def test_get_pet_by_id(obj_id):
    get_pet_endpoint = GetPet()
    get_pet_endpoint.get_pet_by_id(obj_id)
    get_pet_endpoint.check_response_id(obj_id)
    get_pet_endpoint.status_code_is_200()

def test_get_pet_by_invalid_id():
    get_pet_endpoint = GetPet()
    get_pet_endpoint.get_pet_by_id(3735735473)
    get_pet_endpoint.status_code_is_404()

def test_get_pet_by_string_id():
    get_pet_endpoint = GetPet()
    get_pet_endpoint.get_pet_by_id("invalid_id")
    get_pet_endpoint.status_code_is_404()

@pytest.mark.parametrize('payload_update', payloads.payload_update)
def test_update_pet(payload_update, obj_id):
    update_pet_endpoint = UpdatePet()

    payload_update['id'] = obj_id
    update_pet_endpoint.update_pet_by_id(payload_update)
    update_pet_endpoint.status_code_is_200()
    update_pet_endpoint.chek_id_pet_in_response(obj_id)
    update_pet_endpoint.chek_name_pet_in_response(payload_update['name'])
    update_pet_endpoint.check_status_in_response(payload_update['status'])

def test_delete_pet(obj_id):
    delete_pet_endpoint = DeletePet()
    get_pet_endpoint = GetPet()

    delete_pet_endpoint.delete_pet_by_id(obj_id)
    delete_pet_endpoint.status_code_is_200()
    get_pet_endpoint.get_pet_by_id(obj_id)
    get_pet_endpoint.status_code_is_404()
 

def test_delete_non_existent_pet():
    delete_pet_endpoint = DeletePet()
    delete_pet_endpoint.delete_pet_by_id(999999)
    delete_pet_endpoint.status_code_is_404()