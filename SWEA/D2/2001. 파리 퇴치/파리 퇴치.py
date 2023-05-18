t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_num = 0
    for k in range(n-m+1):
        for h in range(n-m+1):
            num = 0
            # m*m 값들의 합
            for i in range(k,m+k):
                for j in range(h,m+h):
                   num += arr[i][j]
            if num > max_num: max_num = num

    print(f'#{tc} {max_num}')