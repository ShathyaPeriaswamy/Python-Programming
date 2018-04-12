a=raw_input()
b=a.split('.')
w=len(b)
count=0
for i in range(0,w):
	s=b[i]
	t=len(s)
	for j in range(0,t):
		r=s[j]
		if r.isdigit():
			count=count+1
print count
