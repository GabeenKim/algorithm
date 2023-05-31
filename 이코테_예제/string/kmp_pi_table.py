pattern = "ababaaba"

pi = [0]*len(pattern)
i= 0

for j in range(1, len(pattern)):
    while i > 0 and pattern[i]!=pattern[j]:
        i = pi[i-1]
        print(i)
    if pattern[i] == pattern[j]:
        i += 1
        pi[j] = i
        print(i,j)
print(pi)