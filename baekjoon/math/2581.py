import math

m = int(input())
n = int(input())

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

prime_num = []

for i in range(m, n + 1):
    if i == 1: continue
    if is_prime(i):
        prime_num.append(i)

if len(prime_num) == 0:
  print(-1)
else : 
  print(sum(prime_num))
  print(min(prime_num))
