h, m = input().split()

H = int(h)
M = int(m)

if M>=45:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1, M+15)
elif M<45 and H==0:
    print(23, M+15)
