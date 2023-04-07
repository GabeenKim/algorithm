s = input()

# 현재 위치 
column = int(ord(s[0]))-int(ord('a'))+1
row = int(s[1])

# 나이트 좌표 
coord = [(-1,2),(1,2),(-1,-2),(1,-2),(-2,1),(-2,-1),(2,1),(2,-1)]

count = 0
for i in coord:
  # 이동할 위치 확인
  n_row = row + i[0]
  n_column = column + i[1]
  
  #해당 범위 안에 있으면 카운팅
  if n_row <=8 and n_row >=1 and n_column <= 8 and n_column >=1:
    count += 1

print(count)