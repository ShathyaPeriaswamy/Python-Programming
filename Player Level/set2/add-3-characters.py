a=raw_input()
c=[]
for i in a:
  if(ord(i)>96) and (ord(i)<119):
   b=chr(ord(i)+3)
  elif(ord(i)==120):
     b=chr(123-ord(i)+94)
  elif(ord(i)==121):
     b=chr(123-ord(i)+96)
  elif(ord(i)==122):
     b=chr(123-ord(i)+98)
  else:
    if(ord(i)>64) and (ord(i)<88):
     b=chr(ord(i)+3)
    elif(ord(i)==90):
     b=chr(90-ord(i)+67)
    elif(ord(i)==89):
     b=chr(90-ord(i)+65)
    elif(ord(i)==88):
     b=chr(90-ord(i)+63)
  c.append(b)
k="".join(c)
print k
