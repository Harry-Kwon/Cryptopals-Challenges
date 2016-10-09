import p3_SingleByteXOR

fileName = raw_input("enter file name: ")

sourceFile = open(fileName, 'r')
sources = str(sourceFile.read()).split('\r\n')

bestScore = 99999999
bestSource = ""
bestText = ""

for s in sources:
	text, score = p3_SingleByteXOR.decipherSingleXOR(s)
	if score < bestScore:
		bestScore = score
		bestText = text
		bestSource = s

print(bestSource + "\n" + bestText + "\n" + str(bestScore))
