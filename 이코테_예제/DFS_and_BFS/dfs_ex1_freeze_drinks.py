def dfs_ice(x, y):
    if x<0 or x>=n or y<0 or y>=m : 
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs_ice(x-1,y)  #상
        dfs_ice(x+1,y)  #하
        dfs_ice(x,y-1)  #좌
        dfs_ice(x,y+1)  #우
        return True 
    else : return False 

n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

count = 0

# 모든 지점에 대해서 얼음 덩어리 개수 확인 
for row in range(n):
    for col in range(m):
        if dfs_ice(row,col) == True:
            count+=1

print(count)