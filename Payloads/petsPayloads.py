import uuid

def new_pet_payload():
	pet_name = f"pet-name-{uuid.uuid4().hex}"

	return {
		"name": pet_name,
		"photo_url": "string",
  		"category": {
    		"name": "Cats"
  		},
  		"status": "available"
	}

def pet_pending_payload():
	pet_name = f"pet-name-{uuid.uuid4().hex}"

	return {
		"name": pet_name,
		"photo_url": "string",
  		"category": {
    		"name": "Cats"
  		},
  		"status": "pending"
	}

def pet_sold_payload():
	pet_name = f"pet-name-{uuid.uuid4().hex}"

	return {
		"name": pet_name,
		"photo_url": "string",
  		"category": {
    		"name": "Cats"
  		},
  		"status": "sold"
	}

def nonexistent_category_payload():
	pet_name = f"pet-name-{uuid.uuid4().hex}"
	category = f"{uuid.uuid4().hex}"

	return {
		"name": pet_name,
		"photo_url": "string",
  		"category": {
    		"name": category
  		},
  		"status": "available"
	}