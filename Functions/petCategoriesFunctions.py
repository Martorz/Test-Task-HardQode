import requests
from requests.auth import HTTPBasicAuth

#class categoryFunctions:
ENDPOINT = "http://91.210.171.73:8080/api/"
AUTHENTICATION = HTTPBasicAuth('admin', 'admin')

def create_category(payload):
	return requests.post(ENDPOINT + "category/", json=payload, auth=AUTHENTICATION)

def get_category(category_ID):
	return requests.get(ENDPOINT + f"category/{category_ID}", auth=AUTHENTICATION)

def delete_category(category_ID):
	return requests.delete(ENDPOINT + f"category/{category_ID}", auth=AUTHENTICATION)

def update_category(category_ID, payload):
	return requests.put(ENDPOINT + f"category/{category_ID}/", json=payload, auth=AUTHENTICATION)

def get_all_categories(limit = None, offset = None):
	query = ""
	if limit != None and offset != None:
		query = f"?limit={limit}&offset={offset}"
	elif limit != None:
		query = f"?limit={limit}"
	elif offset != None:
		query = f"?offset={offset}"
	return requests.get(ENDPOINT + f"category/{query}", auth=AUTHENTICATION)
