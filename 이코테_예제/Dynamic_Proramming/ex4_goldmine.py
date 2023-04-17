# 한 줄로 입력받은 값을 n*m 사이즈로 만들기 
for t in range(int(input())):
 
    n,m = map(int,input().split())
    arr =list(map(int,input().split()))

    #1차원 입력 값 -> 2차원 DP테이블로 초기화
    d =[]
    index = 0
    for i in range(n):
        d.append(arr[index:index+m])
        index += m
        
    # m-1번씩 각 열 확인하기 
    for j in range(1,m):
        #행 하나씩 왼위, 왼, 왼아 확인 
        for i in range(n):
            # 왼위 
            if i == 0 : left_up = 0
            else : left_up = d[i-1][j-1]
            # 왼아
            if i == n-1 : left_down = 0
            else : left_down = d[i+1][j-1]
            # 왼 
            left = d[i][j-1]
            #점화식
            d[i][j] = max(left_up,left,left_down)+d[i][j]

    # m-1열에서 최댓값 = 최적의 해 
    max_num = 0
    for i in range(n):
        max_num = max(max_num, d[i][m-1])
    print(max_num)