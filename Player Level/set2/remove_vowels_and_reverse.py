a=raw_input()
c=[]
d=[]
for j in a:
  c.append(j)
for i in c:
  if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
    c.remove(i)
f=c[::-1]
print "".join(f)
