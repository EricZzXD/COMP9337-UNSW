import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)  # generate pub and priv key

publickey = key.publickey()  # pub key export for exchange

print('=' * 100)
plain_text = 'abcdefghijklmnopqrst'
print("Plaintext is: ", plain_text)
# print

cipher_text = publickey.encrypt(plain_text, 32)  # message to encrypt is in the above line 'encrypt this message'
print('Plaintext encrypted using Public Key is:', cipher_text)
# print
# decrypted code below
decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
print('Ciphertext decrypted with Private key is', decrypted)
print('=' * 100)
