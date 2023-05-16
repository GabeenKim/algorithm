for _ in range(1,11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum=[]

    # row, col
    for i in range(100):
        row_sum, col_sum = 0, 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if j == 99 :
                max_sum.append(row_sum)
                max_sum.append(col_sum)
    # diagonal
    diagonal_left, diagonal_right = 0, 0
    for i in range(100):
        diagonal_left += arr[i][i]
        diagonal_right += arr[i][99-i]

    print(f'#{tc} {max(max_sum)}')