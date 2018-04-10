a=int(raw_input())
b=raw_input().split()
num=int(b[0])
for i in range(1,a):
	if(num<int(b[i])):
		num=int(b[i])
print num
