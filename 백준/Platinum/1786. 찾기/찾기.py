import sys
input = sys.stdin.readline

def get_pi(p):
  pi = [0] *len(p) 
  j = 0
  for i in range(1,len(p)):
    while j> 0 and p[i]!= p[j]:
      j = pi[j-1]
    if p[i] == p[j]:
      j += 1
      pi[i] = j
  return pi

def kmp(t,p):
  pi = get_pi(p)

  i = 0 
  cnt = 0
  loca= []

  for j in range(len(t)):
    while i>0 and t[j] != p[i]:
      i = pi[i-1]
    if t[j]==p[i]:
      if i == len(p)-1:
        cnt += 1
        loca.append(j-len(p)+2)
        #이렇게 해야지 겹쳐서 동일한 것도 보장됨.
        i = pi[i]
      else: 
        i+=1
  return cnt, loca

t = input().rstrip()
p = input().rstrip()

cnt, loca = kmp(t,p)
print(cnt)
print(*loca)