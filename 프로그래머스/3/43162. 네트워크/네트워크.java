class Solution {
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        visited = new boolean[n];
        
        for(int i=0;i< n;i++){
            if(!visited[i]){
                answer++;
                dfs(i, computers);
            }
        }
        
        return answer;
    }
    
    public void dfs(int x, int[][] arr){
        visited[x] = true;
        for(int i=0;i<arr.length;i++){
            if(!visited[i] && arr[x][i]==1) dfs(i, arr);
        }
    }
}
//방문하지 않은 컴퓨터가 있으면 새로운 네트워크로 간주함. 
//dfs로 헤당 컴퓨터와 연결된 모든 컴퓨터들을 탐색하면서 방문 처리