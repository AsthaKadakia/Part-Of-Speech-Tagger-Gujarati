f = open('MixTrain.txt','rb')
g = open('MixTrain2.txt','wb')

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
			if (len(fields) != 3):			
				if d !=i:					
					g.write(line)
	i = i+1
