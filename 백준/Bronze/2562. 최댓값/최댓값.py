arr = []

for i in range(9):
    arr.append(int(input()))

maxn = max(arr)
print(maxn)
print(arr.index(maxn) + 1)