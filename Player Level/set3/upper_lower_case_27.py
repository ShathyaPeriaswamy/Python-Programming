a=raw_input()
t=[]
for i in a:
  if(i.islower()):
    v=i.upper()
    t.append(v)
  else:
    v=i.lower()
    t.append(v)
k="".join(t)
print k
