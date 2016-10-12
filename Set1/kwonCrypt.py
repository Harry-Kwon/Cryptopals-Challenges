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
		pText = singleXOR(sourceText, x)
		score = rateString(pText)
		if(score > bestScore):
			bestScore = score
			bestKey = x
			bestPText = pText
	return bestPText, chr(bestKey), bestScore

def findSingleXOR(sources):
	bestScore = -1
	bestSource = ""
	bestText = ""

	for s in sources:
		text, key, score = decryptSingleXOR(s) 
		if score > bestScore:
			bestText = text
			bestScore = score
			bestSource = s

	return bestSource, bestText, bestScore


def repeatXOR(plainText, key):
	ciphertext = ""
	for i in range(0, len(plainText)):
		ciphertext += chr(ord(plainText[i]) ^ ord(key[i%len(key)]))
	return ciphertext

