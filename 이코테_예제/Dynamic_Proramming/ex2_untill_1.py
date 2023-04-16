n = int(input())
d = [0] * 30001

#보텀업으로 DP 진행
for i in range(2,n+1):
    #현재에서 -1 경우
    d[i] = d[i-1]+1
    #2,3,5 각각 나누어 떨어지는 경우가 존재하면 값이 적은 것으로 업데이트 될 수 있도록 구현 
    if i % 2 == 0:
      d[i] = min(d[i],d[i//2]+1)
    if i % 3 == 0 :
      d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0 :
      d[i] = min(d[i],d[i//5]+1)
print(d[n])