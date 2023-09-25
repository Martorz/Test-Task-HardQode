import requests

ENDPOINT = "http://91.210.171.73:8080/api/"

def test_can_call_endpoint():
	response = requests.get(ENDPOINT)
	assert response.status_code == 200