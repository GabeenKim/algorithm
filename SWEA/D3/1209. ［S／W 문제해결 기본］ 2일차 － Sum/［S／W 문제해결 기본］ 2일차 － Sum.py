for _ in range(1,11):
    tc = int(input())
    arr = [[0]*100 for _ in range(100)]

    for i in range(100):
        arr[i] = list(map(int, input().split()))

    sum = 0
    max_sum=[]
    diagonal_left , diagonal_right = 0,0
    for i in range(100):
        for j in range(100):
            sum += arr[i][j]
            if j == 99 :
                max_sum.append(sum)
                sum = 0
            if i == j :
                diagonal_left += arr[i][j]
    for i in range(100):
        for j in range(100):
            sum += arr[j][i]
            if j == 99 :
                max_sum.append(sum)
                sum = 0
            if i == j:
                diagonal_right += arr[j][i]

    print(f'#{tc} {max(max(max_sum),diagonal_right,diagonal_left)}')