a,b,c=raw_input().split()
s=len(a)
r=len(b)
c=int(c)
count=0
if(s==r):
  for i in range (s):
    if(a[i]!=b[i]):
      count=count+1
    else:
      count=count
  if(count==c):
    print 'yes'
  else:
    print 'no'
      
