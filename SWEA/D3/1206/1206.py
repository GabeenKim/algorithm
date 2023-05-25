for test_case in range(1,11):
    n = int(input())
    building = list(map(int, input().split()))
    sum_light = 0

    for i in range(2,n-2) : 
        left_max = max(building[i-2],building[i-1])
        right_max = max(building[i+2],building[i+1])
        max_one = max(left_max, right_max)
 
        if building[i] > max_one :
            sum_light += (building[i] - max_one)
 
    print(f'#{test_case} {sum_light}')