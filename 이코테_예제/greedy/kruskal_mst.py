#특정 원소가 속한 집합을 찾기 
def find_parent(parent,x) :
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합 union
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else : 
        parent[a] = b

#노드의 개수, 간선의 개수 입력받기
v, e = map(int,input().split())
parent = [0]* (v+1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수 
edge = []
result = 0

for i in range(1, v+1):
    parent[i] = i

#모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int,input().split())
    #비용 순으로 정리하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edge.append((cost,a,b))

#간선은 비용 순으로 오름차순 정렬
edge.sort()

for i in edge:
    cost, a, b = i
    #간선을 확인하여 사이클이 발생하지 않은 경우만 집합에 포함 
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a,b)
        result += cost 

print(result)