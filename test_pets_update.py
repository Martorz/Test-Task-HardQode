import requests
import Payloads.petsPayloads as payloads
import Functions.petsFunctions as petsFunctions

# Позитивные тесты

def test_can_update_pet():
	#Создаем питомца
	payload = payloads.new_pet_payload()
	create_pet_response = petsFunctions.create_pet(payload)
	assert create_pet_response.status_code == 201

	#Обновляем питомца
	pet_ID = create_pet_response.json()['id']
	new_payload = payloads.new_pet_payload()
	update_pet_response = petsFunctions.update_pet(pet_ID, new_payload)
	assert update_pet_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при обновлении
	get_pet_response = petsFunctions.get_pet(pet_ID)
	assert get_pet_response.status_code == 200
	get_pet_data = get_pet_response.json()
	assert get_pet_data['id'] == pet_ID
	assert get_pet_data['name'] == new_payload['name']
	assert get_pet_data['photo_url'] == new_payload['photo_url']
	assert get_pet_data['status'] == new_payload['status']
	assert get_pet_data['category']['name'] == new_payload['category']['name']

