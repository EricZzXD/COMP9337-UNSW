import hashlib

#initializing string
print('='*100)
str = "SHA1 Clear text"
  
result = hashlib.sha1(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 digest is : ") 
print(result.hexdigest())
print('='*100)
