g,i=raw_input().split()
d=len(i)
z=int(i)
if i.isdigit():
	a=int(i)
	r=0
	l=0
	for t in range(g,a+1):
		while(a!=0):
			b=t%10
			r=(r*0)+b**d	
			l+=r
			t=t/10
		print l
else:
	print "invalid input"
