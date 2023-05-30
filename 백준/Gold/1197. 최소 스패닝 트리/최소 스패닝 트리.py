import sys
input = sys.stdin.readline

# 서로소 집합 자료구조 이용하기 
# 특정 원소가 속한 집합 찾기 
def find_parent(parent,x):
  # 현재 노드가 루트노드가 아니라면 
  if parent[x] != x:
    # 부모 테이블의 값이 다시 루트가 되게 하여 재귀호출
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 합집합 
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  # 더 큰 루트노드가 작은 루트노드를 가리키도록 
  if a < b :
    parent[b] = a
  else : 
    parent[a] = b


v, e = map(int,input().split())
parent = [0]*(v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수 생성 
edge = []
result = 0

for i in range(1,v+1):
  parent[i] = i

#모든 간선에 대한 정보 입력 받기 
for _ in range(e):
  a,b,c = map(int,input().split())
  edge.append((c,a,b))

#간선을 비용 순으로(튜플에서 c가 기준) 오름차순 정렬
edge.sort()

for i in edge:
  c, a, b = i
  #간선 확인 후 사이클 발생X인 경우에만 집합에 포함
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += c

print(result)
