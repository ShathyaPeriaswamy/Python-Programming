n=raw_input()
if n.isdigit():
	l=int(n)
	if(l>60):
		s= l%60
		t= l/60
		print ('{0} {1}'.format(t,s))
		
else:
	print "no"
