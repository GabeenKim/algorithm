#기본적인 최소공통 조상 알고리즘
import sys
input = sys.stdin.readline

#노드의 개수
n= int(input())

parent = [0] * (n+2)    #부모노드
d = [0] * (n+1)         #각 노드까지의 깊이
c = [0] * (n+1)         #각 노드의 깊이가 계산되었는지 여부 
graph = [[]for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#dfs -> 모든 노드에 대해 깊이 계산
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:    #이미 깊이 구했으면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

#A와 B의 최소공통조상을 찾는 함수 
def lca(a,b):
    #먼저 깊이가 동일하도록 맞춰줌
    while d[a] != d[b] :
        if d[a] > d[b] :
            a = parent[a]
        else :
            b = parent[b]
    #노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a 

dfs(1,0) #루트 노드는 1번 

#두 노드의 쌍
m = int(input())

for i in range(m):
    a, b = map(int,input().split())
    print(lca(a,b))


        