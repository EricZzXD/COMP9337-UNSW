from Crypto.Cipher import AES
from Crypto import Random

import binascii
import codecs

import sys
import time


# Read file and check whether the CBC block
def readfile(path):
    CBC_block = 8
    CBC_Padding = "\x00"
    f = open(path, mode='r', encoding="latin-1").read()

    # Detect if Need to do padding
    if len(f) % CBC_block == 0:
        return f
    else:
        # Check how many Byte does the File missing & Padding Null byte according
        missingPad = CBC_block - (len(f) % CBC_block)
        f += missingPad * CBC_Padding
        return f


# AES CBC Encryption
def encrypt_AES(iv, key, plain_text):
    des_Encrypt = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = des_Encrypt.encrypt(plain_text)
    return cipher_text


# DES CBC Description
def decrypt_AES(iv, key, cipher_text):
    des_Decrypt = AES.new(key, AES.MODE_CBC, iv)
    decrypt_cipher = des_Decrypt.decrypt(cipher_text)
    return decrypt_cipher


if __name__ == '__main__':
    # Input File & Pre-define IV and KEY
    inputfile = sys.argv[1]
    iv = Random.get_random_bytes(16)
    key = Random.get_random_bytes(16)

    # Read File & encoding before encryption so that only record the Encryption time
    file_Value = readfile(inputfile).encode("latin-1")

    # Encryption
    E_start_Time = time.time()
    Cipher_Text = encrypt_AES(iv, key, file_Value)
    Encryption_Time = time.time() - E_start_Time

    # Decryption
    D_start_Time = time.time()
    decrypt_AES(iv, key, Cipher_Text)
    Decryption_Time = time.time() - D_start_Time

    # Print Value
    print("=" * 100)
    print("Encryption: ", "AES CBC")
    print("Input file Name: ", inputfile)
    print("Input file Length: ", len(readfile(inputfile)))
    print("Encryption Time Used: ", Encryption_Time)
    print("Decryption Time Used: ", Decryption_Time)
    print('\n')
