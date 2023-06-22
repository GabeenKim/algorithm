def solution(n, computers):
    
    def dfs(i,computers,visited):
        visited[i] = 1
        
        for j in range(n):
            if not visited[j] and computers[i][j] :
                dfs(j,computers,visited)     
        return 
    
    answer = 0
    visited = [0]*n
    
    for i in range(n):
        if not visited[i] :
            dfs(i,computers,visited)
            answer += 1
            
    return answer