import os
home = "/home/sarafnikit/Guj/POS/Temp1"
temp = "/home/sarafnikit/Guj/POS/Temp2"

j = 1
for f in os.listdir(home):
	p = os.path.join(home,f)
	q = os.path.join(temp,f)

	f = open(p,'rb')
	g = open(q,'wb')

	for line in f:
		#for words in line:		
		words = line.split()
		for word in words:	
			ws = word.split("\\")
			s = ' '.join(ws)
			s = s + '\n'		
			g.write(s)
		g.write("\n")
	print "File " + str(j) + " done"	
	j = j + 1
	f.close()
	g.close()

