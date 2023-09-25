import requests
import Payloads.petsPayloads as payloads
import Functions.petsFunctions as petsFunctions

# Позитивные тесты

def test_can_create_pet():
	#Создаем питомца
	payload = payloads.new_pet_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201
	
	#Выводим питомца
	pet_ID = create_pet_response.json()['id']
	get_pet_response = petsFunctions.get_pet(pet_ID)
	assert get_pet_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при создании
	get_pet_data = get_pet_response.json()
	assert get_pet_data['name'] == payload['name']
	assert get_pet_data['photo_url'] == payload['photo_url']
	assert get_pet_data['status'] == payload['status']
	assert get_pet_data['category']['name'] == payload['category']['name']

def test_create_pet_pending():
	#Создаем питомца
	payload = payloads.pet_pending_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201
	
	#Выводим питомца
	pet_ID = create_pet_response.json()['id']
	get_pet_response = petsFunctions.get_pet(pet_ID)
	assert get_pet_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при создании
	get_pet_data = get_pet_response.json()
	assert get_pet_data['name'] == payload['name']
	assert get_pet_data['photo_url'] == payload['photo_url']
	assert get_pet_data['status'] == payload['status']
	assert get_pet_data['category']['name'] == payload['category']['name']

def test_create_pet_sold():
	#Создаем питомца
	payload = payloads.pet_sold_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201
	
	#Выводим питомца
	pet_ID = create_pet_response.json()['id']
	get_pet_response = petsFunctions.get_pet(pet_ID)
	assert get_pet_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при создании
	get_pet_data = get_pet_response.json()
	assert get_pet_data['name'] == payload['name']
	assert get_pet_data['photo_url'] == payload['photo_url']
	assert get_pet_data['status'] == payload['status']
	assert get_pet_data['category']['name'] == payload['category']['name']

# Негативные тесты

def test_create_pet_no_body():
	payload = None
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 400

def test_create_pet_nonexistent_category():
	payload = payloads.nonexistent_category_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 404

def test_create_pet_with_existing_name():
	payload = payloads.new_pet_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201

	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 400

