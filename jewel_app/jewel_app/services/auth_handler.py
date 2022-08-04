import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer

SECRET_KEY = "3a691f714afe6a512f2f36f45255a9cb4ce82821474cf22da3040f7e1fb5cfaf"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 1

context  = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])

def hash_password(self, password):
    return self.context.hash(password)

def verify_password(self, password, hashed_password):
    return self.context.verify(password, hashed_password)

def generate_token(self, user_id):
    now = datetime.utcnow()
    payload = {
        'sub': user_id,
        'iat': now,
        'exp': now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm='HS256')
    return token

def verify_token(self, token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return payload

def get_user_id_from_token(self, token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return payload['sub']
