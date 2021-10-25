from Crypto.PublicKey import RSA
import pprint
key = RSA.generate(2048)
public_key = key.publickey().exportKey('PEM')

print("Public Key: ")
print("="*80)
pprint.pprint(public_key.decode())
print("="*80)

file = open(r"Public Key\public_key.txt", "wb")
file.write(public_key)
file.close()

