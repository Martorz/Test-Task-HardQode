import requests
import Functions.petCategoriesFunctions as categoryFunctions
import Payloads.categoryPayloads as payloads

# Позитивные тесты

def test_can_delete_category():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Удаляем категорию
	category_ID = create_category_response.json()['id']
	delete_category_response = categoryFunctions.delete_category(category_ID)
	assert delete_category_response.status_code == 204

	#Проверяем, чтобы категория удалилась
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 404

# Негативные тесты

def test_delete_no_id():
	category_ID = None
	delete_category_response = categoryFunctions.delete_category(category_ID)
	assert delete_category_response.status_code == 400

def test_delete_incorrect_type_id():
	category_ID = 3,14
	delete_category_response = categoryFunctions.delete_category(category_ID)
	assert delete_category_response.status_code == 400

def test_delete_negative_int_id():
	#Создаем категорию
	payload = payloads.new_category_payload()
	create_category_response = categoryFunctions.create_category(payload)
	assert create_category_response.status_code == 201

	#Удаляем категорию
	category_ID = create_category_response.json()['id']
	delete_category_response = categoryFunctions.delete_category(-category_ID)
	assert delete_category_response.status_code == 400

	#Проверяем, чтобы категория не удалилась
	get_category_response = categoryFunctions.get_category(category_ID)
	assert get_category_response.status_code == 200

def test_delete_nonexistent_category():
	category_ID = 2147483646
	delete_category_response = categoryFunctions.delete_category(category_ID)
	assert delete_category_response.status_code == 404