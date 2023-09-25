import requests
from requests.auth import HTTPBasicAuth

#class categoryFunctions:
ENDPOINT = "http://91.210.171.73:8080/api/"
AUTHENTICATION = HTTPBasicAuth('admin', 'admin')

def get_token(payload):
	return requests.post(ENDPOINT + "token/auth/", json=payload, auth=AUTHENTICATION)