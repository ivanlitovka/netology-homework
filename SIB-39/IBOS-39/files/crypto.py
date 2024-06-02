from Crypto.Cipher import AES
from Crypto import Random
import hashlib

key = b'123'
key = hashlib.sha256(key).digest()
print(key)

cipher = AES.new(key, AES.MODE_EAX)

nonce = cipher.nonce
data = b'Secret text'
ciphertext, tag = cipher.encrypt_and_digest(data)
print("Ciphertext:", ciphertext)


for i in range(0,1000):
    t = bytes(str(i), encoding='utf-8')
    key_dec=hashlib.sha256(t).digest()
    cipher = AES.new(key_dec, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    print("\nSecret text:",i,":",plaintext)
