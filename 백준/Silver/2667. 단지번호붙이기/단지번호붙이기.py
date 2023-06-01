import sys
input = sys.stdin.readline

def check_one(x,y):
  global value
  if x<0 or y<0 or x>=n or y>=n : 
    return False
    
  if arr[x][y] == 1: 
    arr[x][y] = 0
    value += 1
    check_one(x-1,y)  #상
    check_one(x+1,y)  #하
    check_one(x,y-1)  #좌
    check_one(x,y+1)  #우
    return True
  else : return False

n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]

cnt,value = 0,0
house = []

for i in range(n):
  for j in range(n):
    if check_one(i,j) == True:
      house.append(value)
      cnt += 1
      value = 0

print(cnt)
house.sort()
for i in house:
  print(i)