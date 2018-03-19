i=raw_input()
s=1
if i.isdigit():
	a=int(i)
	for x in range (1,a+1):
		s*=x
	print s
else:
	print "invalid input"
