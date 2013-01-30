import sys

f = open(sys.argv[1],"rb")
g = open(sys.argv[2],"rb")
h = open(sys.argv[3],"wb")

for line1,line2 in zip(f,g):
	a = line1.split()
	b = line2.split()
	try:
		c = a[0] + " " + b[0] + "\n"
	except:
		c = "\n"
	h.write(c)
