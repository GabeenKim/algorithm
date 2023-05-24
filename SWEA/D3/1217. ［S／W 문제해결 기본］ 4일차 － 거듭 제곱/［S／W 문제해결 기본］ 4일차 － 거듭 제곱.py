def power(n,m):
    global ans
    if m <=0 : return
    ans *= n
    power(n,m-1)

for tc in range(1, 11):
    t = int(input())
    n, m = map(int,input().split())
    ans = 1
    power(n,m)
    print(f'#{tc} {ans}')