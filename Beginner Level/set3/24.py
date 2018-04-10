a=int(raw_input())
b=raw_input().split()
for i in range(a):
	for j in range(a):
		if(int(b[i])<int(b[j])):
			temp=b[i]
			b[i]=b[j]
			b[j]=temp
for i in range(a):
	print b[i],
