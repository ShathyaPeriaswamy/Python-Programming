while True:
	n=raw_input()
	if (n=="exit"):
		print "Terminated"
		break
	else:
		print "Enter the numbers"
		a=int(raw_input())
		b=int(raw_input())
		print "1.Addition " + "2.Subtraction " + "3.Multiplication " + "4.Division " + "5.Exponential"
		c=int(raw_input())
		if(c==1):
			print (a+b)
		elif(c==2):
			print (a-b)
		elif(c==3):
			print (a*b)
		elif(c==4):
			print (a/b)
		elif(c==5):
			print (a**b)
		else:
			"no"
