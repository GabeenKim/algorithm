def dfs(graph,v,visted):
  #현재노드 방문 처리
  visited[v]=True
  print(v,end='')

  for i in graph[v]:
    #현재노드와 연결된 노드 중, 방문 X인 것이 있으면 재귀함수 이용해, 계속해서 탐색
    if not visited[i] :
      dfs(graph,i,visited)   

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
dfs(graph,1,visited)