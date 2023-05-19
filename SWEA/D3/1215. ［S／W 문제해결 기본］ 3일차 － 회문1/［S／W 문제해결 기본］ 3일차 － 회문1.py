for tc in range(1,11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    for i in arr:
        for j in range(9-length):
            s = i[j:j + length]
            comp = s[::-1]
            if comp == s :
                cnt += 1

    for i in zip(*arr):
        for j in range(9-length):
            s2 = i[j:j + length]
            comp2 = s2[::-1]
            if comp2 == s2 :
                cnt += 1

    print(f'#{tc} {cnt}')