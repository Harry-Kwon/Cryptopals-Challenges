import charFreqs

hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
cText = hexString.decode("hex")

def xor_string_with_byte(t, b):
	return "".join(chr(ord(tx) ^ b) for tx in t)

def rateString(px):
	freqs = {}
	for i in range(0, 256):
		freqs[chr(i)] = 0.0

	for x in px:
		if (ord(x) >= 65 and ord(x) <= 90):
			freqs[chr(ord(x)+32)] += 1.0/float(len(px))	
		else:
			freqs[chr(ord(x))] += 1.0/float(len(px))
	score = 0.0
	for x in freqs.keys():
		if ord(x) >= 97 and ord(x) <= 122:
			score += abs(charFreqs.frequencies[x] - freqs[x])
		else:
			score += freqs[x]
	return(score)

bestScore = 9999999.0
bestText = ""
for x in range(0, 256):
	pText = xor_string_with_byte(cText, x)
	score = rateString(pText)
	print("\n" +str(x) + " : " + str(score) + " : " + pText)
	if(score < bestScore):
		bestScore = score
		bestText = pText
print(bestText)
print(bestScore)
