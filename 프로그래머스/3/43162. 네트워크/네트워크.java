import java.util.*;
class Solution {
    public int[] visited;
    public int solution(int n, int[][] computers) {
        visited = new int[n];
        int answer=0;
        
        for(int i=0; i<n; i++){
            if(visited[i]==0){
                answer++;
                dfs(i,n, computers);   
            }
        }
        return answer;
    }
    
    public void dfs(int node, int n, int[][] computers){
        visited[node]=1;
                
        for(int j=0; j<n;j++){
            if(computers[node][j]==1 && visited[j]==0){
                dfs(j,n, computers);
            }
        }
    }
}