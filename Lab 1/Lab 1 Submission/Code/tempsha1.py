import hashlib
import time
import sys


def readfile(path):
    f = open(path, mode='r', encoding="latin-1").read()
    return f


if __name__ == '__main__':
    inputfile = sys.argv[1]
    # Read file
    f = readfile(inputfile)

    # Start Encryption and Calculate Used time
    startTime = time.time()
    result = hashlib.sha1(f.encode())
    UsedTime = time.time() - startTime

    # printing the equivalent hexadecimal value.
    print("=" * 100)
    print("Encryption: ", "SHA1")
    print("Input file Name: ", inputfile)
    print("Input file Length: ", len(readfile(inputfile)))
    print("Encryption Time Used: ", UsedTime)
    print("Encryption Result: ", result.hexdigest())
    print('\n')
