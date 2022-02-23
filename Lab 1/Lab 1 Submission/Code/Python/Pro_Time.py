import sys
import os

iv = "fedcba9876543210"
key = "40fedf386da13d57"

fileArray = ["TestFile/test16.txt", "TestFile/test64.txt", "TestFile/test512.txt", "TestFile/test4096.txt",
             "TestFile/test32768.txt", "TestFile/test262144.txt", "TestFile/test2047152.txt"]

#
for i in fileArray:
    os.system("python tempdes.py " + iv + " " + key + " " + i + " output.des")
