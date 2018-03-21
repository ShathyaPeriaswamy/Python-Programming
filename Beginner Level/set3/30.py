n,m=raw_input().split()
a,b=raw_input.split()
if n.isdigit():
	if(n>=a and m>=b):
		s=n-a
		t=m-b
		print ('{0} {1}'.format(s,t))
	else:
		s=a-n
		t=b-m
		print ('{0} {1}'.format(s,t))
		
else:
	print "no"
