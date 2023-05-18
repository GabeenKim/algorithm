t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    ans = 0
    for i in range(n//2+1):
        start = (n// 2) - i
        end = (n// 2) + i + 1
        num = arr[i][start : end]
        for j in num :
            ans += j

    for i in range(n//2+1,n):
        start = i - (n // 2)
        end = n - start
        num = arr[i][start: end]
        for j in num:
            ans += j
    print(f'#{tc} {ans}')
