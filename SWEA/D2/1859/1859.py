t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    price = list(map(int, input().split()))
    benefit = 0
    max_num = price[-1]
    for i in range(len(price) - 2, -1, -1):
        if price[i] > max_num:
            max_num = price[i]
        else:
            benefit += max_num - price[i]

    print(f'#{test_case} {benefit}')