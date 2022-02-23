README

In this folder you will find the following files:

- tempdes.py : is a sample code for encrypting / decrypting using DES
- temprsa.py : is a sample code for encrypting / decrypting using RSA
- tempsha1.py : is a sample code for digest generation using SHA1
- tempHMAC.py : is a sample code for signature generation using HMAC
- tempaes.py : is a sample code for encrypting / decrypting using AES
- RSA_Key_Generation.py : is a sample code for generating public/private key pair using RSA
- lorem.txt : is a sample text file whose signature is generated in tempHMAC.py file
- test.txt,test2.txt,test3.txt: are sample plain text files to test your code
- test.des,test2.des,test3.des: are DES encrypted versions of files test.txt,test2.txt,test3.txt. 
  Key and IV values used are as follows.
	- Key = 40fedf386da13d57 (Hexadecimal values)
	- IV  = fedcba9876543210 (Hexadecimal values)
- In the linux command line, execute "python tempdes.py", where tempdes.py 
is the python script.

