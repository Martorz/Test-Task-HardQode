import requests
import Functions.petCategoriesFunctions as categoryFunctions
import Payloads.categoryPayloads as payloads

# Позитивные тесты

def test_can_update_category():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Обновляем категорию
	category_ID = create_category_response.json()['id']
	new_payload = payloads.new_category_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при обновлении
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200
	get_category_data = get_category_response.json()
	assert get_category_data['id'] == category_ID
	assert get_category_data['name'] == new_payload['name']

# Негативные тесты

def test_update_category_with_existing_name():
	#Создаем первую категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Создаем вторую категорию
	second_payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(second_payload)
	assert create_category_response.status_code == 201

	#Меняем имя второй категории на имя первой
	category_ID = create_category_response.json()['id']
	update_category_response = categoryFunctions.update_category(category_ID, payload)
	assert update_category_response.status_code == 400

	#Сверяем полученные данные с теми, которые использовали при создании второй категории
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200
	get_category_data = get_category_response.json()
	assert get_category_data['id'] == category_ID
	assert get_category_data['name'] == second_payload['name']

def test_update_category_no_id():
	category_ID = None
	new_payload = payloads.new_category_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 400

def test_update_nonexistent_category():
	category_ID = 2147483646
	new_payload = payloads.new_category_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 400

def test_update_category_empty_payload():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Обновляем категорию
	category_ID = create_category_response.json()['id']
	new_payload = payloads.empty_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 400

	#Сверяем полученные данные с теми, которые использовали при создании
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200
	get_category_data = get_category_response.json()
	assert get_category_data['id'] == category_ID
	assert get_category_data['name'] == payload['name']

# Граничные значения

def test_update_category_less_than_border_payload():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Обновляем категорию
	category_ID = create_category_response.json()['id']
	new_payload = payloads.less_than_border_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при обновлении
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200
	get_category_data = get_category_response.json()
	assert get_category_data['id'] == category_ID
	assert get_category_data['name'] == new_payload['name']

def test_update_category_equals_border_payload():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Обновляем категорию
	category_ID = create_category_response.json()['id']
	new_payload = payloads.equals_border_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 200

	#Сверяем полученные данные с теми, которые использовали при обновлении
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200
	get_category_data = get_category_response.json()
	assert get_category_data['id'] == category_ID
	assert get_category_data['name'] == new_payload['name']

def test_update_category_more_than_border_payload():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Обновляем категорию
	category_ID = create_category_response.json()['id']
	new_payload = payloads.more_than_border_payload()
	update_category_response = categoryFunctions.update_category(category_ID, new_payload)
	assert update_category_response.status_code == 400

	#Сверяем полученные данные с теми, которые использовали при создании
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200
	get_category_data = get_category_response.json()
	assert get_category_data['id'] == category_ID
	assert get_category_data['name'] == payload['name']