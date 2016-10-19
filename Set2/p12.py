from kwonCrypt import *
from random import random

rKey = randomKey(16)
f = open("s12.txt", "r")
source = str(f.read()).decode("base64")

def randAesOracle(pText):
	p = pText + source
	return ecbEncrypt(p, rKey)

def findBlockSize(oracle):
	m = "A"
	l = len(oracle(m))
	while len(oracle(m)) == l:
		m += "A"
	return len(oracle(m))-l

def findSaltByte(oracle, known, bSize):
	blocks = len(known)/bSize+1
	s = "A"*(blocks*bSize-len(known)-1)
	m = oracle(s)
	for i in range(256):
		if oracle(s+known+chr(i))[:blocks*bSize] ==  m[:blocks*bSize]:
			return chr(i)
	return "" 
def findSalt(oracle):
	saltSize = len(oracle(""))
	bSize = findBlockSize(oracle)
	mode = detectBlockOracleMode(oracle)
	if mode == "ECB":
		salt = ""
		next = findSaltByte(oracle, salt, bSize) 
		while next != "":
			salt += next
			next = findSaltByte(oracle, salt, bSize)
	return salt

print findSalt(randAesOracle)
