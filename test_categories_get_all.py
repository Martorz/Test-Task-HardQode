import requests
import Functions.petCategoriesFunctions as categoryFunctions

def test_can_get_all_categories():
	get_all_categories_response = categoryFunctions.get_all_categories()
	assert get_all_categories_response.status_code == 200