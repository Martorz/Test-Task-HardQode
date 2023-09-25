import requests
import Payloads.petsPayloads as payloads
import Functions.petsFunctions as petsFunctions

# Позитивные тесты

def test_can_get_all_pets():
	get_all_pets_response = petsFunctions.get_all_pets()
	assert get_all_pets_response.status_code == 200

