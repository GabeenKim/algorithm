N = int(input())
plans = input().split()
x,y = 1,1

#동북서남 좌표
dx = [0,-1,0,1]
dy = [1,0,-1,0]
direction=['R','U','L','D']

for k in plans:
  for i in direction:
    # 계획서의 방향 좌표만큼 더해서 다음 위치 좌표 구하기
    if i == k:
      coord = direction.index(i)
      nx = x + dx[coord]
      ny = y + dy[coord]
      
      # NxN사이즈 벗어나면 무시하기 
      if nx<1 or ny <1 or nx>5 or ny>5:
        continue
      
      x, y = nx ,ny  # 현재 좌표 설정
   
print(x,y)