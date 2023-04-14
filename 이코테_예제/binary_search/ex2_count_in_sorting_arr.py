from bisect import bisect_left, bisect_right

def count_by_range(array,x):
    right_index = bisect_right(array,x)
    left_index = bisect_left(array,x)
    return right_index - left_index

n , x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_range(array, x)
if count == 0:
    print(-1)
else :
    print(count)