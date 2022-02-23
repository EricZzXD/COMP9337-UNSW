from pypresent import Present

# Encrypting with a 128-bit key:
# -------------------------------
key = "0123456789abcdef0123456789abcdef".decode('hex')
cipher = Present(key)

print('='*100)
print('Key used: ', key.encode('hex'))


print('='*100)
# Plain text should be even-length
plain_text = "0123456789abcdef".decode('hex') # <- 16 bytes
print("Plaintext is: ", plain_text.encode('hex'))

cipher_text = cipher.encrypt(plain_text)
print("Ciphertext is: ", cipher_text.encode('hex'))

msg = cipher.decrypt(cipher_text)
print("Decrypted message: ", msg.encode('hex'))
print('='*100)
