from Crypto.Cipher import AES
from Crypto import Random

cbc_key = Random.get_random_bytes(16)
print('=' * 100)
print('Key used: ', [x for x in cbc_key])

iv = Random.get_random_bytes(16)
print("IV used: ", [x for x in iv])
print('=' * 100)
aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

plain_text = 'hello world 1234'  # <- 16 bytes
print("Plaintext is: ", plain_text)

cipher_text = aes1.encrypt(plain_text)
print("Ciphertext is: ", cipher_text)

msg = aes2.decrypt(cipher_text)
print("Decrypted message: ", msg)
print('=' * 100)
