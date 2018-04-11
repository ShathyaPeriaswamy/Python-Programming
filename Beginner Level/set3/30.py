n,m=raw_input().split()
a,b=raw_input().split()
n=int(n)
m=int(m)
a=int(a)
b=int(b)
if(n>a):
	print n-a,
else:
	print a-n,
if(m>b):
	print m-b,
else:
	print b-m
