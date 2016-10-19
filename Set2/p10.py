from kwonCrypt import *


f = open("s10.txt", "r")
source = str(f.read()).decode("base64")

w = open("sol10.txt", "w+")
w.write(cbcDecrypt(source, "YELLOW SUBMARINE", "\x00"*16))
