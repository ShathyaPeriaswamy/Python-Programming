a=raw_input()
m=0
n=1
for i in range(int(a)):
  b=raw_input()
  for j in b:
    if (j>m):
      m=j
  print m,
  for t in b:
    if (j<=n):
      n=j
  print n
   
