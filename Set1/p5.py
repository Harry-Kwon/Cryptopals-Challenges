import repeatXOR

f = open("p5Source.txt", "r")
t = str(f.read())

c = repeatXOR.repeatXOR(t, "ICE")
print("\n"+c)
