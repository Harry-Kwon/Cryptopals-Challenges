import charFreqs

def xor(bx, by):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bx, by))

def singleXOR(t, b):
	return "".join(chr(ord(tx) ^ b) for tx in t)

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

def decipherSingleXOR(sourceText):
	cText = sourceText.decode("hex")
	bestScore = -1
	bestText = ""
	for x in reversed(range(0, 256)):
		pText = singleXOR(cText, x)
		score = rateString(pText)
		if(score > bestScore):
			bestScore = score
			bestText = pText
	return(bestText, bestScore)

def findSingleXORKey(sourceText):
	bestScore = -1
	bestKey = 0
	for x in reversed(range(0, 256)):
		pText = singleXOR(sourceText, x)
		score = rateString(pText)
		if(score > bestScore):
			bestScore = score
			bestKey = x
	return chr(bestKey)

def findSingleXORFile(fileName, delim):
	sourceFile = open(fileName, 'r')
	sources = str(sourceFile.read()).split(delim)
	bestScore = -1
	bestSource = ""
	bestText = ""

	for s in sources:
		text, score = decipherSingleXOR(s) 
		if score > bestScore:
			bestScore = score
			bestText = text
			bestSource = s

	return bestSource, bestText, bestScore


def repeatXOR(plainText, key):
	ciphertext = ""
	for i in range(0, len(plainText)):
		ciphertext += chr(ord(plainText[i]) ^ ord(key[i%len(key)]))
	return ciphertext

def repeatXORFile(key, inFile, outFile):	
	f = open(inFile, "r")
	t = str(f.read())
	cText = repeatXOR(t, key)

	o = open(outFile, "w+")
	o.write(cText)
