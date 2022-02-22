#Following code reads its source file and computes an HMAC signature for it:
import hmac
secret_key = 'secret-shared-key-goes-here'
digest_maker = hmac.new(secret_key)#in your code replace key
f = open('lorem.txt', 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
finally:
    f.close()

digest = digest_maker.hexdigest()
print('='*100)
print("HMAC digest generated for \"lorem.txt\" file is:", digest)
print('='*100)
