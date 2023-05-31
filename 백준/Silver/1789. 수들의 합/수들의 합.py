s = int(input())

cnt = 0
sum = 0

for i in range(1,s+1):
  sum += i 
  cnt += 1
  if sum > s :
    num = sum - s 
    sum -= num 
    cnt -= 1
  if sum == s:
    break 
print(cnt)