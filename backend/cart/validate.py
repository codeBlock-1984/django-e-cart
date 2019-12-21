import jwt

secret_key = 'secret_key'

def generate(payload):
    if payload:
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token

def validate(token):
    if token:
        try:
            valid_token = jwt.decode(token, secret_key)
            return True
        except:
            return False
    else:
        return False

