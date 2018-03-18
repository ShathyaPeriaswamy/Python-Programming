a,b=raw_input().split()
if a.isdigit() and b.isdigit():
  c=int(a)
  d=int(b)
  print pow(c,d)
else:
  print "invalid input"
