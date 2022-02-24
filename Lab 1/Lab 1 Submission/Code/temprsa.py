import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import sys
import time

from Crypto.Cipher import PKCS1_OAEP


def readfile(path):
    f = open(path, mode='rb')
    return f.read()


if __name__ == '__main__':
    # Pre-define Value to get Encryption Key
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)  # generate pub and priv key
    publickey = key.publickey()  # ----> Use key to generate Public Key
    encryptor = PKCS1_OAEP.new(publickey)  # ---> Encryptor
    decryptor = PKCS1_OAEP.new(key)      # ---> Decryptor for decryption

    # Read file to get Input value (Plaintext)
    inputfile = sys.argv[1]
    f = readfile(inputfile)

    # Start encryption
    Enc_Start = time.time()
    encrypted = encryptor.encrypt(f)
    Enc_Used = time.time() - Enc_Start

    # Start Decryption
    Decry_Start = time.time()
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    Decry_Used = time.time() - Decry_Start

    # Print Value
    print("=" * 100)
    print("Encryption: ", "RSA")
    print("Input file Name: ", inputfile)
    print("Input file Length: ", len(readfile(inputfile)))
    print("Encryption Time Used: ", Enc_Used)
    print("Decryption Time Used: ", Decry_Used)
    print('\n')


# random_generator = Random.new().read
# key = RSA.generate(1024, random_generator)  # generate pub and priv key
#
# publickey = key.publickey()  # pub key export for exchange
#
# print('=' * 100)
# plain_text = 'abcdefghijklmnopqrst'
# print("Plaintext is: ", plain_text)
# # print
#
# cipher_text = publickey.encrypt(plain_text, 32)  # message to encrypt is in the above line 'encrypt this message'
# print('Plaintext encrypted using Public Key is:', cipher_text)
# # print
# # decrypted code below
# decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
# print('Ciphertext decrypted with Private key is', decrypted)
# print('=' * 100)
