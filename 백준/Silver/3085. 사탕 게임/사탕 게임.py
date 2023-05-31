#복습 필 
n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0

def find_chr(board):
  max_cnt = 1
  for i in range(n):
    cnt = 1
    for j in range(1,n):
      if board[i][j] == board[i][j-1]:
        cnt +=1 
      else : 
        cnt = 1
      max_cnt = max(max_cnt,cnt)
      
    cnt = 1
    for j in range(1,n):
      if board[j][i] == board[j-1][i]:
        cnt +=1 
      else : 
        cnt = 1
      max_cnt = max(max_cnt,cnt)
  
  return max_cnt   

for i in range(n):
  for j in range(n):
    if j + 1 < n :
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      cnt = find_chr(board)
      ans = max(ans,cnt)
      # 바꾼 것 원래대로 돌려놓기
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

    if i+ 1< n :
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      cnt = find_chr(board)
      ans = max(ans,cnt)
      # 바꾼 것 원래대로 돌려놓기
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)