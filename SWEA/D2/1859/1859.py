# max() 시간복잡도 O(n)임을 유의! 
t = int(input())
for t in range(1, t+ 1):
    n = int(input())
    arr = list(map(int, input().split()))

    benefit = 0
    buy = []
    for i in range(n):
        # 본인을 기준으로 뒤에 큰 값이 있으면 스택에 삽입
        if any(arr[i] < arr[j] for j in range(i + 1, n)):
            buy.append(arr[i])
        else:
            while buy != []:
                benefit += arr[i] - buy.pop()

    print(f'#{t} {benefit}')