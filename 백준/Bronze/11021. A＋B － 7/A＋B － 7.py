import sys

cnt = int(input())
for i in range(cnt):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #' + '{0}: {1}'.format(i+1, a+b))