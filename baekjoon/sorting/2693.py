t = int(input())

for _ in range(t):
  arr_a = list(map(int,input().split()))
  arr_a.sort(reverse=True)
  print(arr_a[2])