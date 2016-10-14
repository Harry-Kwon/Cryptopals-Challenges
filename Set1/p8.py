from kwonCrypt import *

file = open("s8.txt", "r")
sources = str(file.read()).split("\n")

for s in sources:
	s = s.decode("hex")

def dupeRate(s, u):
	ps = s[:len(s)-len(s)%u]
	c = [ps.count(i) for i in [ps[j*u:(j+1)*u] for j in range(0, len(ps)/u)]]
	return float(max(c))/float(len(ps)/u) 

bestRate = 0
bestS = ""
	
for s in sources:
	if len(s)<16:
		continue
	r = dupeRate(s, 16)
	if r > bestRate:
		bestRate = r
		bestS = s 

print bestRate
print [bestS[j*16:(j+1)*16] for j in range(0, len(bestS)/16)]
print bestS
