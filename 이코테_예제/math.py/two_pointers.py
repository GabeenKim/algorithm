#특정한 합을 가지는 부분 연속 수열 찾기 -> 투 포인터 알고리즘 이용

n=5 #데이터의 개수  
m=5 #찾고자 하는 부분합
data = [1,2,3,2,5]

count = 0
interval_sum = 0    #구간 별 부분합을 담을 변수
end = 0             #끝점

#start 시작점을 차례대로 증가시키며 반복
for start in range(n):
    #end를 가능한 만큼 이동
    while interval_sum < m and end < n :
        interval_sum += data[end]
        end += 1    #부분수열의 합이 m보다 작으니 끝점 이동

    if interval_sum == m :
        count += 1
    # while문 탈출? => 부분수열의 합 >= m 따라서 시작점의 데이터 값만큼 부분합에서 빼주고 for문으로 돌아가 시작점 +1
    interval_sum -= data[start]

print(count)
