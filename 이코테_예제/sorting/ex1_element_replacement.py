# n<=100,000 이므로 O(nlogn)시간 복잡도여야 함. 
n , k = map(int,input().split())

array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))

array_a.sort()  #a는 오름차순
array_b.sort(reverse = True)    #b는 내림차순 

for i in range(k):
    #a원소가 b원소보다 작은 경우 스와프
    if array_a[i] < array_b[i]:
        array_a[i],array_b[i] = array_b[i], array_a[i]
    else : 
        break

print(sum(array_a))
  