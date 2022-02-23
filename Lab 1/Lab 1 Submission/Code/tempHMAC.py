import hashlib
import hmac
import time
import sys


def readfile(path):
    f = open(path, mode='rb')
    return f


if __name__ == '__main__':

    # Generate a key for HMAC
    digest_maker = hmac.new("This is a secret key".encode("latin-1"), digestmod=hashlib.md5)

    # Read File
    # inputfile = sys.argv[1]
    inputfile = "test.txt"
    f = readfile(inputfile)

    try:
        while True:
            block = f.read()
            if not block:
                break
            digest_maker.update(block)
    finally:
        f.close()

    # Record the performance of the HMAC
    startTime = time.time()
    digest = digest_maker.hexdigest()
    UsedTime = time.time() - startTime

    # Print Value
    print("=" * 100)
    print("Encryption: ", "HMAC")
    print("Input file Name: ", inputfile)
    print("Input file Length: ", len(readfile(inputfile).read()))
    print("Encryption Time Used: ", UsedTime)
    print("HMAC digest generated: ", digest)
    print('\n')
