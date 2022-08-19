a, b, c = list(map(int, input().split()))

if(a==b==c):
    print(a*1000 + 10000)
elif(a!=b!=c and a!=c):
    print(max(a, b, c)*100)
else:
  if(a==b):
    print(a*100 + 1000)
  else:
    print(c*100 + 1000)