import re
import os

def rep1(m):
	return '_'

def rep2(m):
	return '\\'

home = "/home/sarafnikit/Guj/POS/Data"
temp = "/home/sarafnikit/Guj/POS/Temp1"

j = 1
for f in os.listdir(home):
	p = os.path.join(home,f)
	q = os.path.join(temp,f)

	f = open(p,'rb')
	g = open(q,'wb')
	i = 0
	for line in f:
		if i!=0:
			text = re.sub('htd[0-9]+\s','',line)
			text = re.sub('\.',' .',text)		
			text = re.sub('\s+\.\s+',' .',text)
			text = re.sub('\s\.',' .',text)
			text = re.sub('\-',rep1,text)
			text = re.sub(r' \\',rep2,text)
			text = re.sub('\|',rep2,text)
			g.write(text)
		i = i + 1
	print "File " + str(j) + " done"
	j = j + 1	
	f.close()
	g.close()


