import requests
import Functions.petCategoriesFunctions as categoryFunctions
import Payloads.categoryPayloads as payloads

# Позитивные тесты

def test_can_create_category():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201
	
	#Выводим категорию
	category_ID = create_category_response.json()['id']
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при создании
	get_category_data = get_category_response.json()
	assert get_category_data['name'] == payload['name']

# Негативные тесты

def test_create_empty_category():
	payload = payloads.empty_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 400

def test_create_int_category():
	payload = payloads.int_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 400

def test_create_category_with_existing_name():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Создаем категорию с таким же названием
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 400

# Граничные значения

def test_create_category_less_than_border_payload():
	payload = payloads.less_than_border_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

def test_create_category_equals_border_payload():
	payload = payloads.equals_border_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

def test_create_category_more_than_border_payload():
	payload = payloads.more_than_border_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 400