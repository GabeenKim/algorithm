import sys
input = sys.stdin.readline 

#데이터 개수, 변경횟수, 구간 합 계산 횟수 
n, m, k = map(int,input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

#i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i) :
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result 

#i번째 수를 바뀐 크기(dif) 만큼 더하는 함수
def update(i, dif):
    while i <= n :
        tree [i] += dif
        i += (i & -i)

#start부터 end까지 구간 합을 계산하는 함수 
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i,x)

for i in range(m+k):
    #a==1인 경우 b번째 수를 c로 바꿈 / a==2인 경우 b번째 수부터 c번째 수까지의 합을 구하여 출력.
    a,b,c = map(int,input().split())
    #update의 걍우
    if a == 1:
        #특정 번째 b에서 값이 얼마나 바뀌었는지 c-arr[b]를 파라미터로 넣어줌
        update(b, c-arr[b]) #바뀐크기 dif만큼 적용.
        arr[b] = c
    #구간합 연산인 경우
    else : 
        print(interval_sum(b,c))
