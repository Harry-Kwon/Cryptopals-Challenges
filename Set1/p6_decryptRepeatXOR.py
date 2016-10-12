#!/usr/bin/python

from kwonCrypt import *

def hammingDist(string1, string2):
	xored = xor(string1, string2)
	b = "".join(bin(ord(x))[2:] for x in xored)
	return b.count("1")

def findLowestKeySize(cText):
	lowestScore = 99999999
	lowestKeySize = 999999
	
	for k in range(2, 40):
		numBlocks = len(cText)/k
		keyScore = sum(float(hammingDist(cText[0:k], cText[i*k:i*k+k])) for i in range(len(cText)/k))
		keyScore /= float(numBlocks * k)
		if keyScore < lowestScore:
			lowestScore = keyScore
			lowestKeySize = k

	return lowestKeySize

def decipherRepeatXOR(cText):
	keySize = findLowestKeySize(cText)
	
	bestScore = 9999999
	bestText = ""
	
	blocks = [("".join(cText[i*keySize+j] for i in range( len(cText)/keySize-1)) ) for j in range(keySize)]
		
	key = "".join(findSingleXORKey(b) for b in blocks)
	print str(key)	
	pText = repeatXOR(cText, key)
	score = rateString(pText)
	if score < bestScore:
		bestScore = score
		bestText = pText

	return bestText

inFile = open("s6.txt", "r")
source = str(inFile.read()).decode("base64")

solved = str(decipherRepeatXOR(source))
print solved

outFile = open("sol6.txt", "w+")
outFile.write(solved)
