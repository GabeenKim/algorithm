#복습 필. 조합 이용 
from itertools import combinations

N = int(input())
limit = 9876543210
num = []

#1~10개의 조합 만들기
for i in range(1,11):
  # 0~9로 하나씩 조합 생성
  for comb in combinations(range(0,10),i):
    comb = list(comb)
    comb.sort(reverse=True)
    num.append(int(''.join(map(str, comb))))
    
num.sort()

if N > num.index(limit) : print(-1)
else : print(num[N])