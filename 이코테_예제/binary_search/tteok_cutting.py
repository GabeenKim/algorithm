n, m = map(int,input().split())
array = list(map(int,input().split()))

#탐색 범위 -> 0~데이터 중 최댓값
start = 0
end = max(array)

result = 0

while start <= end :
    total = 0
    mid = (start + end)//2
    
    for i in array:
        if i > mid:         # 잘린 떡 길이 계산 
            total += i-mid
    if total < m :          #잘린 길이의 합이 요구사항보다 작으면 끝값을 중간값을 왼쪽으로 옮김
        end = mid - 1
    else :                  #크다면 시작점을 중간값 오른쪽으로 이동
        result = mid        #최대한 덜 잘랐을 때가 정답이므로 이때 result에 값 저장 
        start= mid+1
      
print(f'높이 h : {result}')