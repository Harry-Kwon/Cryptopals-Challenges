#!/usr/bin/python

import charFreqs

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
