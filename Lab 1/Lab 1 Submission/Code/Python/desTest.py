import binascii
import codecs

from Crypto.Cipher import DES
from Crypto import Random
import sys
import time


# Read file and check whether the CBC block
def readfile(path):
    CBC_block = 8
    CBC_Padding = "\0"
    f = open(path, mode='r', encoding="latin-1").read()

    # Detect if Need to do padding
    if len(f) % CBC_block == 0:
        return f
    else:
        # Check how many Byte does the File missing & Padding Null byte according
        missingPad = CBC_block - (len(f) % CBC_block)
        f += missingPad * CBC_Padding
        return f


# DES CBC Encryption
def encrypt_DES(iv, key, plain_text):
    des_Encrypt = DES.new(key, DES.MODE_CBC, iv)
    cipher_text = des_Encrypt.encrypt(plain_text)
    return cipher_text


# DES CBC Description
def decrypt_DES(iv, key, cipher_text):
    des_Decrypt = DES.new(key, DES.MODE_CBC, iv)
    decrypt_cipher = des_Decrypt.decrypt(cipher_text)
    return decrypt_cipher


if __name__ == '__main__':
    # iv, key, inputfile, outputfile= binascii.unhexlify(sys.argv[1]), binascii.unhexlify(sys.argv[2]), sys.argv[3], sys.argv[4]

    iv = binascii.unhexlify("fedcba9876543210")
    key = binascii.unhexlify("40fedf386da13d57")
    inputfile = "test2.txt"
    CompareFile = "test2.des"

    print("=" * 100)

    # Read File & encoding before encryption so that only record the Encryption time
    file_Value = readfile(inputfile).encode("latin-1")

    # Encryption
    Estart_Time = time.time()
    Cipher_Text = encrypt_DES(iv, key, file_Value)
    Encryption_Time = time.time() - Estart_Time

    # Decryption
    Dstart_Time = time.time()
    DesCipher_Text = decrypt_DES(iv, key, Cipher_Text)
    Decryption_Time = time.time() - Dstart_Time

    # print("Provided Answer:")
    # print(readfile(CompareFile).encode("latin-1"))
    # print("=" * 100)
    # print("Encrypted")
    # print(Cipher_Text)
    # if readfile(CompareFile).encode("latin-1") == Cipher_Text:
    #     print("Match")
    # else:
    #     print("Error")
