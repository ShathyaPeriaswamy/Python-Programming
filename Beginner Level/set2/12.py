n=raw_input()
a=int(n)
z=a
r=0
while(a!=0):
	b=a%10
	r=(r*10)+b
	print r
	a=a/10
if(z==r):
	print "yes"
else:
	print "no"
