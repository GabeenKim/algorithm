#접두사 합 활용해서 구간 합 빠르게 계산하기

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

#접두사 합 배열 먼저 계산
for i in data :
    sum_value += i
    prefix_sum.append(sum_value)

#구간 합 계산 
left = 3
right = 4

print(prefix_sum[right]- prefix_sum[left-1])