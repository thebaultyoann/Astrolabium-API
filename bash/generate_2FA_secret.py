import pyotp
secret_base32 = pyotp.random_base32()
print(secret_base32)