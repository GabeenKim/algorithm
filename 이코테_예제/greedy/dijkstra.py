import sys 
input = sys.stdin.readline #반복문으로 여러줄을 입력 받을 때 시간초과가 발생하지 않으려고
INF = int(1e9)  #무한을 의미하는 값으로 10억 설정

#노드, 간선의 개수를 입력받기
n, m = map(int, input().split())
#시작노드 입력
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]
visited = [False] * (n+1) #방문처리 리스트
#최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

#간선정보 입력받기
for _ in range(m) :
    #a번 노드에서 b번노드로 가는 비용 c
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node ():
    min_vlaue = INF
    index = 0   #가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1, n+1):
        if distance[i] < min_vlaue and not visited[i]:
            min_vlaue - distance[i]
            index = i 
    return index

def dijkstra(start):
    #시작노드에 대해서 초기화
    distance[start]=0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]   #출발노드로부터 인접한 다른 노드까지의 거리를 먼저 최단거리테이블에 갱신.
    #시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now]= True
        
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])

