t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    row, col = 0,0
    cnt = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                row +=1
            if arr[i][j] == 0:
                if row == k :
                    cnt +=1
                row = 0
            if arr[j][i] == 1:
                col +=1
            if arr[j][i] == 0 :
                if col == k:
                    cnt +=1
                col = 0
        # k번째 1이 행or열의 마지막 열에 있을 경우
        if row == k :
            cnt +=1
        if col == k :
            cnt += 1
        row,col = 0,0
    print(f'#{tc} {cnt}')