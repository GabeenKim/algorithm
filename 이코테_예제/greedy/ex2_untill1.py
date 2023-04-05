n, k = map(int,input().split())

result = 0

while True:
  #k의 배수 중 n과 가장 근접한 배수를 알기 위함. 해당 배수가 될 때까지 빼기
  target = (n//k)*k
  result += (n-target)
  n = target

  #n이 k보다 작을 때 더 이상 나눌 수가 없으므로 브레이크
  if n<k:
    break

  #n이 k의 배수이므로 나눔
  result +=1
  n //=k

#1까지 구해야하므로 마지막에 총 횟수에서 -1
result+=(n-1)
print(result)

