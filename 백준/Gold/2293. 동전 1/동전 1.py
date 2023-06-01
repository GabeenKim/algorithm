# 복습 필 
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]

dp = [0]*(k+1)
dp[0] = 1

# 각 화폐단위 씩 k가 되는 값 확인
for c in coin :
  # c동전을 가지고 i원까지의 경우의 수 
  for i in range(c, k+1):
    #이전까지의 dp[i]의 개수 + i-c원일 때 경우의 수 값으로 갱신.(i-c원 값을 만드는 경우에 c원만 더해주면 i원이 되고, 경우의 수만 고려해주니) 
    dp[i] = dp[i] + dp[i-c]

print(dp[k])