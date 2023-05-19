for tc in range(1,11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    col = [[] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            col[i].append(arr[j][i])

    for i in range(8):
        for j in range(9-length):
            s = arr[i][j:j + length]
            s2 = col[i][j:j + length]

            comp = s[::-1]
            comp2 = s2[::-1]

            if comp == s :
                cnt += 1
            if comp2 == s2:
                cnt +=1

    print(f'#{tc} {cnt}')