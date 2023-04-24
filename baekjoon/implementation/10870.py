def fibo(a):
    if a == 0 : return 0 
    if a == 1 or a == 2:
        return 1
    if dp[a] != 0:
        return dp[a]
    return  fibo(a - 1) + fibo(a - 2)
    
a = int(input())
dp = [0] * (a+1)

print(fibo(a))
