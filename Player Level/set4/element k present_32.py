a,b=raw_input().split()
if a.isdigit():
  for i in range(int(a)):
    c=raw_input()
    if b in c:
      print 'Yes'
    else:
      print 'No'
else:
  print 'invalid'
