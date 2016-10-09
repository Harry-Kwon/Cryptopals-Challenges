#input strings encoded in hex
hexString = raw_input("Input Hex Encoded String: ")
hexString2 = raw_input("\nInput 2nd Hex Encoded String: ")

#decode strings to raw bytes
b1 = hexString.decode("hex")
b2 = hexString2.decode("hex")

#xor raw bytes
# for x, y in zip(bx, by) iterates bytes in each string pariwise
# ord(x) ^ ord(y) XORs each byte
# chr(ord(x) ^ ord(y)) to convert to ascii
def xor_binary_strings(bx, by):
	return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(bx, by))

print(xor_binary_strings(b1, b2))
