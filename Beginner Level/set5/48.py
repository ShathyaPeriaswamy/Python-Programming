a=raw_input()
sum=0
for i in range(int(a)):
  b=raw_input().split()
  for j in b:
    sum=sum+int(j)
  t=int(sum)/int(a)
  print t
