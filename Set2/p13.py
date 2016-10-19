from kwonCrypt import *
from random import random

rKey = randomKey(16)
nextUid = 0

def parsekv(k):
	k = ecbDecrypt(k, rKey)	
	print "rawk: " + k
	k = [x.split("=") for x in k.split("&")]
	print k
	return {x[0]:x[1] for x in k}

def profile_for(v):
	global nextUid	
	v = "".join("" if i=="&" else i for i in v)
	s = {"email":v, "uid":nextUid, "role":"user"}
	p = "email="+s["email"]+"&uid="+str(s["uid"])+"&role="+s["role"]
	print p[:32]
	print p[16:32]

	return ecbEncrypt(p, rKey)

def findBlockSize(oracle):
	m = "A"
	l = len(oracle(m))
	while len(oracle(m)) == l:
		m += "A"
	return len(oracle(m))-l

bSize = 16

encUser = profile_for("A"*(2*bSize-len("email="+"&uid=0&role=")))
encAdmin = profile_for("A"*(bSize-len("email=")) + "admin" + " "*(bSize-len("admin")))

encHacked = encUser[:32] + encAdmin[16:32]
print parsekv(encHacked)
