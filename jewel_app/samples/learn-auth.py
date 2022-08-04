from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

cc = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])

hash1 = cc.hash("joshua")
cc.verify('joshua', hash1)

hash2 = cc.hash("joonhwan",scheme="md5_crypt")
print(f'hash2: {hash2}')
cc.verify('joonhwan', hash2)
cc.identify(hash2)
cc.schemes()


user_id = 'winkler'

jwt_secret = "very_very_strong_key"

now = datetime.utcnow()
payload = {
    'sub': user_id,
    'iat': now,
    'exp': now + timedelta(seconds=10),
}
token = jwt.encode(payload=payload, key=jwt_secret, algorithm='HS256')
print(token)

# 아래 코드를 몇번 실행하다 보면 ExpiredSignatureError가 발생한다.
payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
print(payload)



