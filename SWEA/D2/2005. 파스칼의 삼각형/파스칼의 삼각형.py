t = int(input())

for tc in range(1, t+1):
    n = int(input())
    dp = [[0]*i for i in range(1,n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i: dp[i][j] = 1
            else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(f'#{tc}')
    for i in range(n):
        print(*dp[i])