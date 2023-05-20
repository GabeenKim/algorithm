t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [input() for _ in range(n)]

    row, col = 0,0
    cnt = 0

    for i in arr :
        cnt += i.replace(' ', '').split('0').count('1'*k)

    for i in list(zip(*arr)):
        cnt +=''.join(i).split('0').count('1'*k)

    print(f'#{tc} {cnt}')