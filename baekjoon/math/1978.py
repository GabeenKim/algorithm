#소수 판별
import math

n = int(input())
num = list(map(int,input().split()))
count = 0

def is_prime_number(x) :
    #2부터 x-1까지의 모든 수 확인하기 
    for i in range(2,int(math.sqrt(x))+1) :
        #x가 해당 수로 나누어 떨어진다면 소수 아님
        if x % i == 0 :
            return False
    return True
  
for i in num :
  if i == 1 : continue
  if is_prime_number(i):
    count +=1

print(count)