def get_pi(pattern):
  pi = [0]*len(pattern)
  i= 0
  
  for j in range(1, len(pattern)):
    while i > 0 and pattern[i]!=pattern[j]:
      i = pi[i-1]

    if pattern[i] == pattern[j]:
      i += 1
      pi[j] = i
  return pi

def kmp(word, pattern):
  pi = get_pi(pattern)

  # i : word, j : 패턴탐색
  j = 0 
  for i in range(len(word)):
    while j>0 and word[i] != pattern[j]:
      j = pi[j-1]

    if word[i] == pattern[j]:
      if j == len(pattern)-1:
        j = pi[j]
        return 1
      else : 
        j+=1
  return 0

word = input()
pattern = input()

print(kmp(word, pattern))
