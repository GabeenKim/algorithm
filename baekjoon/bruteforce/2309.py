array = [int(input()) for _ in range(9)]
one = 0
two = 0

sum_arr = sum(array)

#2명을 골라서 그 둘의 키를 뺐을 때 나머지 합이 100이 된 경우
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if sum_arr - (array[i] + array[j]) == 100:
            one = array[i]
            two = array[j]

array.remove(one)
array.remove(two)

array.sort()

for i in array:
    print(i)
