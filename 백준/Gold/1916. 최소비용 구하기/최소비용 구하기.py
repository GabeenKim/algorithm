import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
# 모든 간선 벙조를 입력 받기 위한 연결 노드 정보 리스트 graph, 최단 거리 테이블 dist
graph = [[] for _ in range(n+1)]
dist = [INF] * ( n+1 )

for _ in range(m):
  dep, arr, cost = map(int,input().split())
  graph[dep].append((arr,cost))

start, end = map(int,input().split())

def dijkstra(start):
  q= []
  # (최단거리,노드번호)
  heapq.heappush(q,(0,start))
  dist[start] = 0

  while q : 
    distance, now = heapq.heappop(q)
    #현재노드의 최단거리 테이블 속 정보보다 현재 거리 값이 더 크면 continue -> 갱신 전 값이 더 작다면 이미 처리된 노드임. 
    if dist[now] < distance : continue
    # 현재 노드와 연결된 다른 인접 노드들 확인
    for nn, nc in graph[now]:
      cost = distance + nc
      if dist[nn] > cost :
        dist[nn] = cost
        heapq.heappush(q,(cost,nn))

dijkstra(start)

if dist[end] == INF :
  print("INFINITY")
else : 
  print(dist[end])