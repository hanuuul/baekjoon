amount = int(input())
cnt = int(input())
cal = 0

for i in range(cnt):
    a, b = map(int, input().split())
    cal += a*b

if amount == cal:
    print('Yes')
else:
    print('No')
    