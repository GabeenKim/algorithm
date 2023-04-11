from collections import deque

def bfs_maze(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny <0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 방문한 적 X -> 최단 거리 기록(그 전 노드의 비용 +1)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny)) 
    # 가장 우측 하단까지의 최단 거리 반환
    return graph[n-1][m-1]


n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs_maze(0,0))