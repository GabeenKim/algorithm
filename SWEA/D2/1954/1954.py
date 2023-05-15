t = int(input())
# 우하좌상 순
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for test_case in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    row, col = 0, 0
    dir = 0 # 방향 키 제어 변수 우:0, 하:1, 좌:2, 상:3

    for m in range(1, n**2+1):
        arr[row][col] = m
        nrow = row + direct[dir][0]
        ncol = col + direct[dir][1]

        if nrow < 0 or nrow >= n or ncol < 0 or ncol >= n or arr[nrow][ncol]!= 0:
            dir = (dir+1)%4

            nrow = row + direct[dir][0]
            ncol = col + direct[dir][1]

        row, col = nrow, ncol

    print(f'#{test_case}')
    for i in arr:
        print(*i)
    print()
