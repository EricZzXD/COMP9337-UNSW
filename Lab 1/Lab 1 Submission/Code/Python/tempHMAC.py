#Following code reads its source file and computes an HMAC signature for it:
import hmac
import binascii
from Crypto import Random
import time
import sys

def readfile(path):
    f = open(path, mode='rb', encoding="latin-1")
    return f


if __name__ == '__main__':

    # Security Key
    secret_key = binascii.unhexlify("40fedf386da13d57")
    digest_maker = hmac.new(secret_key)

    # Read File
    # inputfile = sys.argv[1]
    inputfile = "TestFile/test4096.txt"

    f = readfile(inputfile)

    try:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    finally:
        f.close()

    startTime = time.time()
    digest = digest_maker.hexdigest()
    UsedTime = time.time() - startTime

    # Print Value
    print("=" * 100)
    print("Encryption: ", "HMAC")
    print("Input file Name: ", inputfile)
    print("Input file Length: ", len(readfile(inputfile).read()))
    print("Encryption Time Used: ", UsedTime)
    print("HMAC digest generated for \"lorem.txt\" file is:", digest)
    print('\n')