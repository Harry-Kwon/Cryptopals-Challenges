def repeatXOR(plainText, key):
	ciphertext = ""
	for i in range(0, len(plainText)):
		ciphertext += chr(ord(plainText[i]) ^ ord(key[i%len(key)]))
	return ciphertext.encode("hex")
