t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    cnt = 0
    s = []

    for row in arr:
        for j in range(n-k+1):
            if row[j:j+k].count(1) == k :
                if j-1 < 0 :
                    if row[j+k] == 0:
                        cnt +=1
                elif j+k >=n :
                    if row[j - 1] == 0:
                        cnt += 1
                else:
                    if row[j-1] == 0 and row[j+k] == 0 :
                       cnt+=1

    for row in zip(*arr):
        for j in range(n - k + 1):
            if row[j:j + k].count(1) == k:
                if j - 1 < 0:
                    if row[j + k] == 0:
                        cnt += 1
                elif j + k >= n:
                    if row[j - 1] == 0:
                        cnt += 1
                else:
                    if row[j - 1] == 0 and row[j + k] == 0:
                        cnt += 1
    print(f'#{tc} {cnt}')