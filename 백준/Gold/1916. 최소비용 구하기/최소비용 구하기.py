# 음인 간선이 없으므로 다익스트라 사용
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  dist[start] = 0

  while q:
    distance, now = heapq.heappop(q)
    if dist[now] < distance:
      continue
    for i in edges[now]:
      cost = distance + i[1]

      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  

n = int(input())
m = int(input())
edges = [[] for i in range(n+1)]

for i in range(m):
  depart, arrival, cost = map(int,input().split())
  edges[depart].append((arrival, cost))

get_de,get_arr = map(int,input().split())

dist = [INF]*(n+1)

dijkstra(get_de) 

if dist[get_arr] ==INF :
    print("-1")
else : 
    print(dist[get_arr])
