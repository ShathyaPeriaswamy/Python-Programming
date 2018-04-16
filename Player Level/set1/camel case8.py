a=raw_input().split()
c=[]
r=[]
for i in a:
  for j in i:
    if(j==j.lower()):
      s=j.upper()
      c.append(s)
    else:
      s=j.lower()
      c.append(s)
  n="".join(c)
  print n,
  c=[]
   
