#큐를 이용한 위상 정렬
from collections import deque

#노드, 간선의 개수 입력받고 모든 노드의 진입차수 0으로 초기화
v, e = map(int,input().split())
indegree = [0]*(v+1)

#간선 정보를 담기 위한 리스트 초기화
graph = [[] for _ in range(v+1)]

#방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    #a -> b 이므로 b의 진입차수 +1
    indegree[b] += 1

#위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    
    #진입 차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0 :
            q.append(i)
    
    while q :
        #큐에서 원소를 꺼내기 -> 위상 정렬 = 큐에서 꺼내진 원소 순서. 따라서 결과 리스트에 원소 삽입 
        now = q.popleft()
        result.append(now)

        #해당 원소에서 나가는 간선 빼기 -> 연결된 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            #새롭게 진입차수가 0이 된 노드 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)
    
    for i in result :
        print(i , end= " ")


topology_sort()