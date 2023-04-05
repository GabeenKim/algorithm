N = int(input())

arr_coin=[500,100,50,10]
count = 0

#화폐단위가 서로 배수임. 따라서 가장 큰 화폐 단위부터 처리하기
for changes in arr_coin:
  count += N//changes
  N %= changes 

print(count)