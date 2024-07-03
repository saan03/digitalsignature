from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key_pair = RSA.generate(2048)

public_key = key_pair.publickey()
private_key = key_pair.export_key()

with open("public_key.pem", "wb") as f:
    f.write(public_key.export_key())

with open("private_key.pem", "wb") as f:
    f.write(private_key)

message = "This is a secret message from Sahana".encode()

encryptor = PKCS1_OAEP.new(public_key)
encrypted_message = encryptor.encrypt(message)

decryptor = PKCS1_OAEP.new(key_pair)
decrypted_message = decryptor.decrypt(encrypted_message)

print("Original message:", message.decode())
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message.decode())
