import random
c=[]
q=[]
h=[]
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
  c.append('_ ')
d="".join(c)
print d
for j in range(3):
  print 'Enter the value'
  p=raw_input()
  if(p in q):
    l=q.index(p)
    c.insert(l,p)
    c.remove('_')
    k=" ".join(c)
    print k
  elif(p==r):
    print 'Congrats you won'
    break
  else:
    print 'Wrong' 
    print 'Need a clue?yes or no?'
    t=raw_input()
    if(t=='yes'):
      clue()
    else:
      print 'Try!!'
      
