# 하루 =24*60*60 =86400뿐이므로 파이썬에서는 매우 빠르게 계산 가능 (1초에 2천만 연산)
# 완전 탐색 문제

N = int(input())

count = 0

#매 시각 안에 3이 포함 되어 있으면 카운트 +
for h in range(N+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s):
        count += 1

print(count)