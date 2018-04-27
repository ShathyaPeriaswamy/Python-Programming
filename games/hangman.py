import random
import string
c=[]
m=[]
q=[]
a=['red','orange','violet','green','blue','black','white','yellow','purple','brown','grey']
r=random.choice(a)
y=a.index(r)
def clue():
  if((y==0) or (y==1)):
    print 'The sun'
  elif((y==2) or (y==8)):
    print 'A decoration flower'
  elif((y==3) or (y==7)):
    print 'Nature'
  elif((y==4) or (y==6)):
    print 'Sky'
  elif((y==5) or (y==9)):
    print 'Dark'
  else:
    print 'old'
for j in r:
  q.append(j)
for i in r:
  c.append('_')
d=" ".join(c)
print d
m=c
for j in (0,len(c)):
  print 'Enter the value'
  p=raw_input()
  if(p in q):
    l=p.index(r)
    c.insert(l+1,p)
    c.remove('_')
    print c
  else:
    print 'wrong'
