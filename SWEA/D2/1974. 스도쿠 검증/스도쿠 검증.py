t = int(input())

for tc in range(1,t+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    ans = False

    def check(arr):
        for x in range(9):
            row = [0] * 10
            col = [0] * 10
            for y in range(9):
                num_row = arr[x][y]
                num_col = arr[y][x]
                # 이미 있는 숫자라면 0을 반환
                if row[num_row]: return 0
                if col[num_col]: return 0
                row[num_row] = 1
                col[num_col] = 1

                # 3x3 행렬 검사
                if x % 3 == 0 and y % 3 == 0:
                    square = [0] * 10
                    for i in range(x, x + 3):
                        for j in range(y, y + 3):
                            num = arr[i][j]
                            if square[num]: return 0
                            square[num] = 1
        return 1

    result = check(arr)
    print(f'#{tc} {result}')



