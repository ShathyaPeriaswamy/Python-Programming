a=int(raw_input())
b=raw_input().split()
for i in range(a):
	for j in range(a):
		if(b[i]<b[j]):
			temp=b[i]
			b[i]=b[j]
			b[j]=temp
z=(a+1)/2-1
print b[z]
