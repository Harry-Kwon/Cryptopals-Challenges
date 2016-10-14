from kwonCrypt import *
from Crypto.Cipher import AES
#test
cipher = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)

file = open("s7.txt", "r")
source = str(file.read()).decode("base64")

print(cipher.decrypt(source))
