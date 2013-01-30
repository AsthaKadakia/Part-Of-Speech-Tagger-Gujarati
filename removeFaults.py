import os

home = "/home/sarafnikit/Guj/POS/Temp2"
final = "/home/sarafnikit/Guj/POS/FinalData"

j = 1
for f in os.listdir(home):
	p = os.path.join(home,f)
	q = os.path.join(final,f)

	f = open(p,'rb')
	g = open(q,'wb')

	i = 0
	c = -1
	d = -2
	for line in f:
		l = line.strip('\n')
		if not l:
			t = '\n'
			g.write(t)
		else:
			fields = l.split(' ')
			if (len(fields)<2):
				c = i
				d = i+1
			else:
				if d !=i:					
					g.write(line)
		i = i+1
	print "File " + str(j) + " done"
	j = j + 1
	f.close()
	g.close()



