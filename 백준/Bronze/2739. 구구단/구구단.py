#첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

n = int(input())

for i in range(1,10):
    print('{0} * {1} = {2}'.format(n, i, n*i))