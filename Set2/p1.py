def PKCS7(s, l):
	s = s+ chr(l-len(s))*(l-len(s))
	return s

print [ord(x) for x in PKCS7("YELLOW SUBMARINE", 20)]
