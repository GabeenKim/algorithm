#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x :
        return find_parent(parent,parent[x])
    return x

#두 원소가 속한 집합을 합치기 
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #일반적으로 더 큰 번호가 작은 번호를 부모로 가리킴
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

#노드, 간선 개수 입력 받기
v, e = map(int,input().split())
parent = [0]*(v+1)

#초기상태 : 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#각 간선에 대해서 union연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end =" ")
for i in range(1, v+1):
    print(find_parent(parent,i), end = " ")

print()

# 부모 테이블 내용 출력하기
print("부모 테이블: ",  end= " ")
for i in range(1,v+1):
    print(parent[i],end= " ")