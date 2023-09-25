import uuid
import random

def new_category_payload():
	ctg_name = f"test-name-{uuid.uuid4().hex}"

	return {
		"name": ctg_name
	}

def empty_payload():
	return {
		"name": ""
	}

def int_payload():
	return {
		"name": random.randint(10000, 99999)
	}

def less_than_border_payload():
	# Кол-во символов: 149
	ctg_name = f"Lorem-ipsum-dolor-sit-amet,-consectetur-adipiscing-elit.-Phasellus-orci-leo,-scelerisque-vitae-leo-sit-amet-molestie-{uuid.uuid4().hex}"
	return {
		"name": ctg_name
	}

def equals_border_payload():
	# Кол-во символов: 150
	ctg_name = f"Lorem-ipsum-dolor-sit-amet,--consectetur-adipiscing-elit.-Phasellus-orci-leo,-scelerisque-vitae-leo-sit-amet-molestie-{uuid.uuid4().hex}"
	return {
		"name": ctg_name
	}

def more_than_border_payload():
	# Кол-во символов: 151
	ctg_name = f"Lorem-ipsum-dolor-sit-amet,---consectetur-adipiscing-elit.-Phasellus-orci-leo,-scelerisque-vitae-leo-sit-amet-molestie-{uuid.uuid4().hex}"
	return {
		"name": ctg_name
	}