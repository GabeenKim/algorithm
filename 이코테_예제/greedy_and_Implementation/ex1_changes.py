N = int(input())

arr_coin=[500,100,50,10]
count = 0

for changes in arr_coin:
  count += N//changes
  N %= changes 

print(count)