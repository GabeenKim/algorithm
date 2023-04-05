N = int(input())
fear_x = list(map(int,input().split()))

fear_x.sort()  #공포도 낮은 것부터 확인하기 위함.

count = 0   #현 그룹에 포함된 모험가의 수
result = 0  #총 그룹의 수 

for i in fear_x:  
  count += 1
  #현 그룹의 모험가의 수가 현 공포도 이상이면 그룹결성
  if count >= i : 
    result +=1
    count = 0
  
print(result)