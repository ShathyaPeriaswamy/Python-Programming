a,b=raw_input().split()
if a.isdigit():
	c=int(a)
	d=int(b)
	for i in range(c,d+1):
		if i>1:
			for x in range (2,i):
				if(i%x)==0:
					break
			else:
				print i,
else:
	print "invalid input"
				
				
