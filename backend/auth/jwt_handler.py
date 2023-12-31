import jwt
import time
from config import JWT_SECRET, JWT_ALGORITHM


# return genrated token
def token_response(token: str):
    return {
        'access token': token
    }

# sigining jwt string
def sign_jwt(user_id: str):
    payload = {
        'user_id' : user_id ,
        'expiration' : time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expiration'] >= time.time() else None
    except:
        return {}