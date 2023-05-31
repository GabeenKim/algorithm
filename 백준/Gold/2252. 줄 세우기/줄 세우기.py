from collections import deque
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
# 진입차수 0으로 초기화
indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):
  # a <- b
  a, b = map(int,input().split())
  graph[a].append(b)
  # a가 b 앞에 서 있으므로 a->b
  indegree[b] += 1

def topology():
  result = [] 
  q = deque()

  # 진입 차수가 0인 노드를 큐에 삽입
  for i in range(1, n+1):
    if indegree[i] == 0 :
      q.append(i)

  while q :
    # 큐에서 원소 꺼내기 
    now = q.popleft()
    result.append(now)

    # 해당 원소에서 나가는 간선 제거. 즉 연결 노드들의 진입차수 -1
    for i in graph[now]:
      indegree[i] -= 1 
      # 새롭게 진입 차수가 0이 된 노드 큐에 삽입
      if indegree[i] == 0 :
        q.append(i)

  print(*result)

topology()