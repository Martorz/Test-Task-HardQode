import uuid

def admin_payload():
	return {
		"username": "admin",
		"password": "admin"
	}

def user_doesnt_exist_payload():
	user_name = f"bad-name-{uuid.uuid4().hex}"
	return {
		"username": user_name,
		"password": "123"
	}

def empty_payload():
	return {
		"username": "",
		"password": ""
	}

def empty_name_payload():
	return {
		"username": "",
		"password": "admin"
	}

def empty_password_payload():
	return {
		"username": "admin",
		"password": ""
	}

def wrong_password_payload():
	return {
		"username": "admin",
		"password": "123"
	}