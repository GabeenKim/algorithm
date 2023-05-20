for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        flag = False
        for j in range(n):
            # N극일 때 플래그 활성화
            if arr[j][i] == 1 : flag = True
            elif arr[j][i] == 2:
                if flag:
                    cnt += 1
                    flag = 0
    print(f'#{tc} {cnt}')