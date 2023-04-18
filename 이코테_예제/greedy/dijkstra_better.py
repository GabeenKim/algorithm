import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드, 간선의 개수 입력 받기
n, m = map(int,input().split())
#시작노드 번호 입력받기
start = int(input())
#연결 노드 정보 리스트
graph = [[] for i in range(n+1)]
#최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    #a번 노드에서 b번노드까지 비용 c 
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

#다익스트라 알고리즘
def dijkstra(start):
    q=[]
    #시작 노드로 가기 위한 최단 거리는 0 -> 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q :
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q)
        #(갱신 전 값이 더 작다면) 이미 처리된 노드면 최단거리 정해진 것. 따라서 무시
        if distance[now] < dist :
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]  #i[1]:거리 값
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]: #i[0] : 노드
                 distance[i[0]] = cost
                 heapq.heappush(q,(cost,i[0]))
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else : 
        print(distance[i])
