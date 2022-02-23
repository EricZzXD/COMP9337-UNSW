import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

print('='*100)

# Create and save the private key in the project folder.
# In practice, the private key would be stored locally with
# the master bot and would not be accessible by anyone else.
# However, this is irrelevant for our botnet simulation as everything is local.
f = open('master_bot_private_key.pem', 'wb')
f.write(key.exportKey('PEM').decode('ascii'))
f.close()
print("Wrote Private key to: \"master_bot_private_key.pem\" file")
# Create and save the public key in the project folder.
# In practice, the public key would be accessible from
# the public server (in this case, the hypothetical pastebot.net).
# However, this is irrelevant for our botnet simulation as everything is local.
f = open('master_bot_public_key.pem', 'wb')
f.write(key.publickey().exportKey('PEM').decode('ascii'))
f.close() 
print("Wrote Public key to: \"master_bot_public_key.pem\" file")

print('='*100)
