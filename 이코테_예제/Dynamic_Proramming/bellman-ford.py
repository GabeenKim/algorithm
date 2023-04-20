import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    #시작 노드에 대해서 초기화
    dist[start] = 0
    #전체 n번의 라운드를 반복
    for i in range(n):
        #매 반복만다 "모든간선" 확인
        for j in range(m):
            current = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            #현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[current] !=INF and dist[next_node] > dist[current] + cost :
                dist[next_node] = dist[current]+cost
                #n번째 라운드에서도 값이 갱신된다면(음수 간선 때문에 계속해서 다음 라운드도 값이 갱신될 수 있음.) 음수 순환이 존재하는 것.
                if i == n-1 :
                    return True
    return False 

n, m = map(int, input().split())

#모든 간선에 대한 정보를 담는 리스트
edges = []
#최단 거리 테이블 무한으로 초기화
dist = [INF]*(n+1)

for _ in range(m) :
    a, b, c = map(int,input().split())
    edges.append((a,b,c))

#벨만포드 알고리즘 
negative_cycle = bf(1) 

if negative_cycle :
    print("-1")
else : 
    #1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력 
    for i in range(2,n+1):
        if dist[i] ==INF :
            print("-1")
        else : 
            print(dist[i])