import secrets
import string

def generate_token(length=16):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

# 16 karakterlik bir token oluştur
token = generate_token()
print("Oluşturulan token:", token)