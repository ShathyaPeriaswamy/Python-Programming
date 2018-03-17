a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
if(a>=b and a>=c):
	d=a
elif(b>=a and b>=c):
	d=b
else:
	d=c
print(d)
