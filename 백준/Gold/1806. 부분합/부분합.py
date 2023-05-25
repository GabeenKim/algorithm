n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 100001
sum_part = arr[0]
start, end = 0,0 

while True:
  if sum_part < s:
    end += 1
    if end == n : break
    sum_part += arr[end]
  else:
    sum_part -= arr[start]
    ans = min(ans, end-start +1)
    start +=1  

print(ans if ans != 100001 else 0)
