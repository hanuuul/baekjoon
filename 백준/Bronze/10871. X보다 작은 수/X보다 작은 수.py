import sys

cnt, maxn = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(cnt):
    if arr[i] < maxn:
        print(arr[i], end=' ')