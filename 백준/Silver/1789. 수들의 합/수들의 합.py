s = int(input())

sum = 0 

for i in range(1,s+1):
  sum += i 
  if sum > s :
    i -= 1
    break  
print(i)