#!/usr/bin/python

import charFreqs
from Crypto.Cipher import AES
from random import random

def xor(bx, by):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bx, by))

def singleXOR(t, b):
	return "".join(chr(ord(tx) ^ ord(b)) for tx in t)

def rateString(px):
	freqs = {}
	score = 0.0
	for i in range(97, 123):
		freqs[i] = 0.0

	for x in px:
		if (ord(x) >= 65 and ord(x) <= 90):
			freqs[ord(x)+32] += 1.0
		elif (ord(x) >= 97 and ord(x) <= 122) :
			freqs[ord(x)] += 1.0
	#divide by number of english characters to get percentage occurence
	for i in range(97, 123):
		freqs[i] = freqs[i] / float(len(px)) * 100.0
	for i in range(97, 123):
		score += abs(charFreqs.freqs[chr(i)] - freqs[i])
	return 1.0/score

def decryptSingleXOR(sourceText):
	bestScore = -1
	bestKey = 0
	bestPText = ""
	for x in reversed(range(0, 256)):
		pText = singleXOR(sourceText, chr(x))
		score = rateString(pText)
		if(score > bestScore):
			bestScore = score
			bestKey = x
			bestPText = pText
	return bestPText, bestKey

def findSingleXOR(sources):
	bestScore = -1
	bestSource = ""
	bestText = ""
	bestKey = ""

	for s in sources:
		text, key = decryptSingleXOR(s)
		score = rateString(text)
		if score > bestScore:
			bestSource = s
			bestText = text
			bestKey = key
			bestScore = score

	return bestSource, bestText, bestKey


def repeatXOR(plainText, key):
	ciphertext = ""
	for i in range(0, len(plainText)):
		ciphertext += chr(ord(plainText[i]) ^ ord(key[i%len(key)]))
	return ciphertext


def hammingDist(string1, string2):
	xored = xor(string1, string2)
	b = "".join(bin(ord(x))[2:] for x in xored)
	return b.count("1")

def findRepeatKeySize(cText):
	lowestHam = 99999999	
	lowestKeySize = 2
	
	for k in range(2, 40):
		#find average hamming distance from dist block to every other block
		numBlocks = len(cText)/k	
		ham = sum(float(hammingDist(cText[0:k], cText[i*k:i*k+k])) for i in range(1, numBlocks))
		ham /= float((numBlocks-1) * k)
		if ham < lowestHam:
			lowestHam = ham 
			lowestKeySize = k
	return lowestKeySize

def decipherRepeatXOR(cText):
	keySize = findRepeatKeySize(cText)
	
	blocks = [("".join(cText[i*keySize+j] for i in range( len(cText)/keySize-1)) ) for j in range(keySize)]	
	key = "".join(chr(decryptSingleXOR(b)[1]) for b in blocks)
	
	pText = repeatXOR(cText, key)

	return pText, key

def dupeRate(s, u=16):
	ps = s[:len(s)-len(s)%u]
	c = {i:ps.count(i)-1 for i in [ps[j*u:(j+1)*u] for j in range(0, len(ps)/u)]}
	return float(sum(c[i] for i in c))/float(len(ps)/u)

def PKCS7(s, l):
	s = s+ chr(l-len(s))*(l-len(s))
	return s

def ecbEncrypt(pText, key="FOOD FOR THOUGHT"):
	cipher = AES.new(key)
	p = PKCS7(pText, len(pText)+16-(len(pText)%16))	
	return "".join(cipher.encrypt(p[16*i:16*(i+1)]) for i in range(len(p)/16))

def ecbDecrypt(cText, key="FOOD FOR THOUGHT"):
	cipher = AES.new(key)
	return "".join(cipher.decrypt(cText[16*i:16*(i+1)]) for i in range(len(cText)/16))

def cbcEncrypt(pText, key="FOOD FOR THOUGHT", iv=" "*16):
	cipher = AES.new(key)
	p = PKCS7(pText, len(pText)+16-(len(pText)%16))
	c = cipher.encrypt(xor(pText[:16], iv))
	for i in range(1, len(p)/16):
		c += cipher.encrypt( xor(c[-16:], p[16*i:16*(i+1)]) ) 
	return c

def cbcDecrypt(cText, key="FOOD FOR THOUGHT", iv=" "*16):
	cipher = AES.new(key)
	p = xor(iv, cipher.decrypt(cText[:16]))
	return p+"".join(xor(cText[16*(i-1):16*i], cipher.decrypt(cText[16*i:16*(i+1)])) for i in range(1, len(cText)/16))
	
def randomKey(l):
	return "".join(chr(int(random()*256)) for i in range(l))

def detectBlockOracleMode(oracle):
	testString = "YELLOW SUBMARINE"*200
	s = oracle(testString)
	if dupeRate(s)>0.8:
		return "ECB"
	else:
		return "CBC"
