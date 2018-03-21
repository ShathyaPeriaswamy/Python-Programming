g,i=raw_input().split()
if i.isdigit():
	a=int(i)
	y=int(g)
	for x in range(y,a+1):
		d=len(i)
		r=0
		l=0
		e=x
		while(e>0):
			b=e%10
			r=(r*0)+b**d	
			l+=r
			e=e/10
		if(x==l):
			print l
else:
	print "invalid input"
