t = int(input())

for i in range(t):
    arr = list(str(input()))
    cnt = 0
    score = 0
    for j in arr:
        if j == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score) 