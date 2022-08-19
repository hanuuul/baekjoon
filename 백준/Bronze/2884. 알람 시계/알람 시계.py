H, M = list(map(int, input().split()))

# 일단 M에서 45분 뺌
M -= 45

if(M >= 0):
	# M이 0보다 크거나 같으면 그냥 그대로 출력
    print(H, M)
else:
	# M이 0보다 작으면? H가 1씩 줄어듦 그리고 줄어든 1=60분은 M에게 넘겨줌
    # 근데 만약 H가 0이라면? -1이 아니고 23이 되어야함 (24시 - 1)
    M += 60
    if(H > 0):
    	print(H-1, M)
    else:
    	print(23, M)
