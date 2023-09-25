import requests
import Payloads.petsPayloads as payloads
import Functions.petsFunctions as petsFunctions

# Позитивные тесты

def test_can_delete_pet():
	#Создаем питомца
	payload = payloads.new_pet_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201

	#Удаляем питомца
	pet_ID = create_pet_response.json()['id']
	delete_pet_response = petsFunctions.delete_pet(pet_ID)
	assert delete_pet_response.status_code == 204

	#Проверяем, чтобы категория удалилась
	get_pet_response = petsFunctions.get_pet(pet_ID)
	assert get_pet_response.status_code == 404

# Негативные тесты

def test_delete_no_id():
	pet_ID = None
	delete_pet_response = petsFunctions.delete_pet(pet_ID)
	assert delete_pet_response.status_code == 400

def test_delete_incorrect_type_id():
	pet_ID = 3,14
	delete_pet_response = petsFunctions.delete_pet(pet_ID)
	assert delete_pet_response.status_code == 400

def test_delete_negative_int_id():
	#Создаем питомца
	payload = payloads.new_pet_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201

	#Удаляем питомца
	pet_ID = create_pet_response.json()['id']
	delete_pet_response = petsFunctions.delete_pet(-pet_ID)
	assert delete_pet_response.status_code == 400

	#Проверяем, чтобы питомец не удалился
	get_pet_response = petsFunctions.get_pet(pet_ID)
	assert get_pet_response.status_code == 200

def test_delete_nonexistent_pet():
	pet_ID = 2147483646
	delete_pet_response = petsFunctions.delete_pet(pet_ID)
	assert delete_pet_response.status_code == 404