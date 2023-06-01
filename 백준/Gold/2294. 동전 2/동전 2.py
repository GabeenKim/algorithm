# 복습 필 
import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]

dp = [INF]*(k+1)
dp[0] = 0

for c in coin : 
  for i in range(c, k+1):
    if dp[i-c] != INF:
      dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == INF : print(-1)
else : print(dp[k])