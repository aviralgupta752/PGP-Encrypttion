from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from cryptography.fernet import Fernet
import pprint

file = open("input.txt", "r")
message = str.encode(file.read())
print("\nSECRET MESSAGE:")
print(message)

file.close()


session_key = Fernet.generate_key()

print("\nSESSION KEY:")
pprint.pprint(session_key)

file = Fernet(session_key)
encrypted_message_using_session_key = file.encrypt(message)

public_key = open(r"Public Key\public_key.txt", "rb").read()


print("\nPUBLIC KEY: ")
pprint.pprint(public_key)

rsa_public_key = RSA.importKey(public_key)
rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
encrypted_session_key_using_public_key = rsa_public_key.encrypt(session_key)
encrypted_session_key_using_public_key_encoded = b64encode(encrypted_session_key_using_public_key)


print("\nENCRYPTED MESSAGES")
print("="*120)

print("\nEncrypted_message_using_session_key: ")
pprint.pprint(encrypted_message_using_session_key)

print("\nEncrypted_session_key_using_public_key: ")
pprint.pprint(encrypted_session_key_using_public_key)

file = open(r"Encrypted Message\encrypted_message_using_session_key.txt", "wb")
file.write(encrypted_message_using_session_key)
file.close()

file = open(r"Encrypted Message\encrypted_session_key_using_public_key.txt", "wb")
file.write(encrypted_session_key_using_public_key)
file.close()

file = open(r"Encrypted Message\encrypted_session_key_using_public_key_encoded.txt", "wb")
file.write(encrypted_session_key_using_public_key_encoded)
file.close()

