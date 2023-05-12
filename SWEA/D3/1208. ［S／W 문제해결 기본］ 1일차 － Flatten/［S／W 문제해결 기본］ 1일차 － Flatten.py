for test_case in range(1, 11):
    cnt =  int(input())
    arr = list(map(int,input().split()))
    
    for i in range(cnt,-1,-1):
        max_num = max(arr)
        min_num = min(arr)
        answer = max_num-min_num
        
        if max_num - min_num <= 1:
            answer = max_num - min_num
            break
        else :
            max_idx = arr.index(max_num)
            min_idx = arr.index(min_num)
            
            answer = arr[max_idx] - arr[min_idx] 
            
            arr[max_idx] = max_num-1
            arr[min_idx] = min_num+1
           
    print(f'#{test_case} {answer}')
