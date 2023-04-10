from collections import deque   # BFS - 큐 이용

def bfs(graph, start, visted):
    # 시작 노드를 큐에 삽입
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지     
    while queue:
        # 큐에서 원소 하나 꺼내서 출력
        v = queue.popleft()
        print(v, end = '')

        # 해당 원소와 연결된 노드들 방문 후 큐에 삽입    
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True            
    
# 그래프 : 연결노드를 2차원 리스트로 표현
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False]*9  # 방문처리 리스트
bfs(graph,1,visited)

