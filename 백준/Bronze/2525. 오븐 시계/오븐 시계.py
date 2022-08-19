h, m = input().split()
endTime = int(input())

H = int(h)
M = int(m) + endTime

H += M//60
M %= 60

if(H>23):
    print(H-24, M)
else:
    print(H, M)