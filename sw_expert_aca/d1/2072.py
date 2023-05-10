t = int(input())
 
for j in range(1,t+1) :
    sum_num = 0
    arr = list(map(int, input().split())) 
    for i in arr :
        if i % 2 == 1:
            sum_num += i
    print(f'#{j} {sum_num}')