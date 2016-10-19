from kwonCrypt import *
from random import random

def randomKey(l):
	return "".join(chr(int(random()*256)) for i in range(l))

def randAesOracle(pText):
	p = randomKey(int(random()*6)+5) + pText + randomKey(int(random()*6)+5)
	if random()<0.5:
		print "ecb"
		return ecbEncrypt(p, randomKey(16))
	else:
		print "cbc"	
		return cbcEncrypt(p, randomKey(16), "\xAB"*16)

def detectOracleMode(oracle):
	testString = "YELLOW SUBMARINE"*200
	s = oracle(testString)
	if dupeRate(s)>0.8:
		return "ECB"
	else:
		return "CBC"

print detectOracleMode(randAesOracle)
