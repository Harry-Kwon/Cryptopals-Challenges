from kwonCrypt import *

inFile = open("s6.txt", "r")
s = str(inFile.read()).decode("base64")

solved = str(decipherRepeatXOR(s)[0])
print solved
