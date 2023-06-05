import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

#k원을 만들 수 있는 경우의 수 dp[k]
dp = [0]*(k+1)
dp[0]= 1

for coin in  coins:
  for i in range(coin,k+1):
    dp[i] = dp[i] + dp[i-coin]

print(dp[k])
    