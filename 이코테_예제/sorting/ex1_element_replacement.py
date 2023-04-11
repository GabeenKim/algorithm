def quick_sort(array):
    if len(array) <= 1 : return array
    pivot = array[0]
    tail = array[1::]

    left_side = [x for x in tail if x <=pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot]+ quick_sort(right_side)
  
n , k = map(int,input().split())

array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))

a = quick_sort(array_a)
b = quick_sort(array_b)

for i in range(k):
    a[i],b[-(i+1)] = b[-(i+1)],a[i]

print(sum(a))
  