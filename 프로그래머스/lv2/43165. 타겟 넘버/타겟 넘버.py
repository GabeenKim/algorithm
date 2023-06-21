

def solution(numbers, target):

    def dfs(idx, num):
        nonlocal cnt
        if idx == len(numbers):
            if num == target :
                cnt += 1
            return 
        dfs(idx+1, num+numbers[idx])
        dfs(idx+1, num-numbers[idx])
    
    cnt = 0
    dfs(0,0)

    return cnt