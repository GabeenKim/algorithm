INF = int(1e9)

#노드, 간선 개수 입력받기
n = int(input())
m = int(input())

#2차원 리스트(그래프 표현) 생성 후 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기->자기로 가는 비용은 0으로 초기화 
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b :
            graph[a][b]=0

# 각 간선에 대한 정보를 입력 받고 그 값으로 초기화
for _ in range(m):
    #a에서 b로 가는 비용 c
    a, b, c = map(int,input().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):     # k : 거쳐가는 노드
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


#수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF :
            print("INFINITY")
        else :
            print(graph[a][b],end=" ")
    print()
