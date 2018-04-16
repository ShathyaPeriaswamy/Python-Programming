a,b=raw_input().split()
n=0
for j in range(int(a),int(b)+1):
  if j>1:
    for i in range(2,j):
      if(j%i)==0:
        break
    else:
      n=n+1
print n
