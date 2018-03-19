i=raw_input()
if i.isdigit():
	a=int(i)
	for x in range (1,6):
		print a*x,
else:
	print "invalid input"
