i=raw_input()
z=int(i)
if i.isdigit():
	a=int(i)
	r=0
	l=0
	while(a!=0):
		b=a%10
		r=(r*10)+b
		a=a/10
	if(z==r):
		print "yes"
	else:
		print "no"
else:
	print "invalid input"
