s = input()

result = int(s[0])

for i in range(1,len(s)):
    data = int(s[i])
    #0,1이면 *보다 +가 훨씬 수가 커짐
    if data <= 1 or result<=1:
        result += data
    else :
        result *= data
  
print(result)