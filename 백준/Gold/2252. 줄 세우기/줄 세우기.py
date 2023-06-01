from collections import deque
import sys
input = sys.stdin.readline

def topology():
  #정렬결과. 큐에 삽입되는 순서가 정렬 순서
  result = []
  q = deque()

  # 진입차수가 0인 노드 큐에 삽입
  for i in range(1,n + 1):
    if indegree[i] == 0:
      q.append(i)
  # 큐에서 꺼낸 것을 결과 리스트에 삽입. 연결된 노드들의 진입차수 제거-> 진입차수 0이 된 것 새로이 삽입 반복
  while q:
    now = q.popleft()
    result.append(now)

    for i in edge[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  print(*result)


n, m = map(int, input().split())

#진입차수 변수
indegree = [0] * (n + 1)
#방향 그래프의 간선 정보 입력 받기
edge = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  edge[a].append(b)
  indegree[b] += 1

topology()
