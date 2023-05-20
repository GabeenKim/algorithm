t = int(input())

for tc in range(1,t+1):
    n = int(input())

    arr = [input().split() for _ in range(n)]

    def rotate(arr):
        new = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new[j][n-1-i] = arr[i][j]
        return new

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    print(f'#{tc}')
    for i in range(n):
        print(''.join(arr1[i]), ''.join(arr2[i]), ''.join(arr3[i]))
