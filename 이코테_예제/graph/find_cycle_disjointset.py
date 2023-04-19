# 특정 원소가 속한 집합 찾기 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

#노드, 간선 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False   #사이클 발생 여부

for i in range(e) :
    #간선 선택
    a, b = map(int, input().split())
    #사이클 판별
    if find_parent(parent,a) == find_parent(parent,b) :
        cycle = True
    else : 
        union_parent(parent,a,b)

if cycle :
    print('사이클이 발생했습니다.')
else : 
    print('사이클이 발생하지 않았습니다.')