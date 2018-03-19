i=raw_input()
if i.isdigit():
	a=int(i)
	z=a
	r=0
	l=0
	while(a!=0):
		b=a%10
		r=(r*0)+b
		r=r**d
		l+=r
		a=a/10
	print l
else:
	print "invalid input"
