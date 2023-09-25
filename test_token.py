import requests
import Payloads.tokenPayloads as payloads
import Functions.tokenFunctions as tokenFunctions

# Позитивные тесты

def test_can_get_token():
	payload = payloads.admin_payload()
	get_token_response = tokenFunctions.get_token(payload)
	assert get_token_response.status_code == 200

# Негативные тесты

def test_token_user_does_not_exist():
	payload = payloads.user_doesnt_exist_payload()
	get_token_response = tokenFunctions.get_token(payload)
	assert get_token_response.status_code == 400

def test_token_empty_payload():
	payload = payloads.empty_payload()
	get_token_response = tokenFunctions.get_token(payload)
	assert get_token_response.status_code == 400

def test_token_empty_name_payload():
	payload = payloads.empty_name_payload()
	get_token_response = tokenFunctions.get_token(payload)
	assert get_token_response.status_code == 400

def test_token_empty_password_payload():
	payload = payloads.empty_password_payload()
	get_token_response = tokenFunctions.get_token(payload)
	assert get_token_response.status_code == 400

def test_token_wrong_password_payload():
	payload = payloads.wrong_password_payload()
	get_token_response = tokenFunctions.get_token(payload)
	assert get_token_response.status_code == 400