import requests
from requests.auth import HTTPBasicAuth

#class categoryFunctions:
ENDPOINT = "http://91.210.171.73:8080/api/"
AUTHENTICATION = HTTPBasicAuth('admin', 'admin')

def create_pet(payload):
	return requests.post(ENDPOINT + "pet/", json=payload, auth=AUTHENTICATION)

def get_pet(pet_ID):
	return requests.get(ENDPOINT + f"pet/{pet_ID}/", auth=AUTHENTICATION)

def delete_pet(pet_ID):
	return requests.delete(ENDPOINT + f"pet/{pet_ID}/", auth=AUTHENTICATION)

def update_pet(pet_ID, payload):
	return requests.put(ENDPOINT + f"pet/{pet_ID}/", json=payload, auth=AUTHENTICATION)

def get_all_pets(limit = None, offset = None):
	query = ""
	if limit != None and offset != None:
		query = f"?limit={limit}&offset={offset}/"
	elif limit != None:
		query = f"?limit={limit}/"
	elif offset != None:
		query = f"?offset={offset}/"
	return requests.get(ENDPOINT + f"pet/{query}", auth=AUTHENTICATION)
