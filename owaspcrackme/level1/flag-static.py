#python2

from Crypto.Cipher import AES
import base64
secret = base64.b64decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=")
key = "8d127684cbc37c17616d806cf50473cc".decode('hex')
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(secret)

print plaintext
