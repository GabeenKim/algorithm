n = int(input())
arr = list(map(int,input().split()))
#순서를 뒤집어서 LIS 문제로 변환 
arr.reverse()

#초기 길이를 위해 값이 1 크기가 n인 dp테이블 초기화
d = [1]*n

#LIS 알고리즘 
for i in range(1,n):
  for j in range(i):
    if arr[i]>arr[j]:
      d[i] = max(d[i],d[j]+1)

#열외해야 하는 인원 수 출력
print(n-max(d))