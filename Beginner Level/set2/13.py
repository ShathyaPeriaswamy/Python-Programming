n=raw_input()
if n.isdigit():
	a=int(n)
	for i in range (2,a/2):
		if((a%i)==0):
			x=1
			break
		else:
			x=0
	if(x==0):
		print "yes"
	else:
		print "no"
else:
	print "invalid input"
