import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

#k원을 만들 수 있는 경우의 수 dp[k]
dp = [INF]*(k+1)
dp[0]=0

for coin in  coins:
  for i in range(coin,k+1):
    dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k]!= INF : print(dp[k])
else : print(-1)