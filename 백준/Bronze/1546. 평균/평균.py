cnt = int(input())
score = list(map(int, input().split()))
newscore = []

for i in range(cnt):
    newscore.append(score[i]/max(score)*100)

print(sum(newscore)/cnt)