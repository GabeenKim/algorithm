for tc in range(1,11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    std = length // 2 if length%2== 0 else (length//2)+1

    for i in arr:
        for j in range(9-length):
            if i[j+length-1 : j+length-1-std : -1] == i[j:j + std]:
                cnt += 1

    for i in zip(*arr):
        for j in range(9-length):
            if i[j+length-1 : j+length-1-std : -1] == i[j:j + std]:
                cnt += 1

    print(f'#{tc} {cnt}')