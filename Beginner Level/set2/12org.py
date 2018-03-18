i=raw_input()
a=int(i)
z=a
r=0
while(a!=0):
	b=a%10
	r=(r*10)+b
	a=a/10
if(z==r):
	print "yes"
else:
	print "no"
