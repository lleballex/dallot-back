from dallot.settings import SECRET_KEY

import jwt
from datetime import datetime, timedelta


def get_auth_token(user_id):
	token_data = {
		'user_id': user_id,
		'exp': datetime.now() + timedelta(days=7)
	}
	return jwt.encode(token_data, SECRET_KEY)

def decode_auth_token(token):
	try:
		token_data = jwt.decode(token, SECRET_KEY)
	except jwt.exceptions.DecodeError:
		return None

	return token_data['user_id']