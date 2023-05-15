t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    score = list(map(int,input().split()))
    cnt  = [0]*101 # 0부터 100점까지의 개수를 담을 리스트

    for i in range(1000):
        cnt[score[i]] += 1

    #최고빈도수가 동일한 수들 중 점수가 높은 것 택하기
    result = list(filter(lambda x: cnt[x] == max(cnt), range(100)))
    print(f'#{test_case} {max(result)}')