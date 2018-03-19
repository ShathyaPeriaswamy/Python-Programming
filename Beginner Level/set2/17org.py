i=raw_input()
d=len(i)
z=int(i)
if i.isdigit():
	a=int(i)
	r=0
	l=0
	while(a!=0):
		b=a%10
		r=(r*0)+b**d
		l+=r
		a=a/10
	if(z==l):
		print "yes"
	else:
		print "no"
else:
	print "invalid input"

