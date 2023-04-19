import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

#다익스트라 알고리즘 
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #(시간, 노드) 튜플로 삽입
    distance[start]= 0

    while q :
        dist, now_node = heapq.heappop(q)
        #최단거리 테이블에 저장되어 있는게 큐에서 꺼낸 것보다 작으면 이미 최단거리 결정된 것. 따라서 무시! 
        if distance[now_node] < dist :
            continue 

        for i in graph[now_node]:
            # 연결된 노드를 확인해서 해당 노드를 거쳐가는 것이 더 효과적인지 판별
            cost = dist +i[1] 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

#도시, 통로, 출발도시 입력받기
n, m, c = map(int, input().split())

graph = [[]for _ in range(n+1)]
distance = [INF]*(n+1)

# 간선 비용 입력받기 
for i in range(m):
    # x->y까지의 시간 z
    x, y, z = map(int,input().split())
    graph[x].append((y, z)) #(노드,시간)

dijkstra(c)

count = 0 
max_dist = 0

for i in distance:
  if i != INF:
    count += 1
    max_dist = max(max_dist, i)
    
print(count -1, max_dist)
  