class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n]; // 1차원 배열로 방문 여부 체크

        // 모든 컴퓨터를 순회
        for (int i = 0; i < n; i++) {
            // 아직 방문하지 않은 컴퓨터라면
            if (!visited[i]) {
                // 새로운 네트워크 발견!
                answer++;
                // 해당 컴퓨터와 연결된 모든 컴퓨터를 DFS로 탐색
                dfs(i, computers, visited);
            }
        }
        return answer;
    }
    
    // DFS 함수
    public void dfs(int node, int[][] computers, boolean[] visited) {
        // 현재 노드(컴퓨터)를 방문 처리
        visited[node] = true;

        // 현재 노드와 연결된 다른 노드들을 탐색
        for (int i = 0; i < computers.length; i++) {
            // 연결되어 있고 아직 방문하지 않았다면
            if (computers[node][i] == 1 && !visited[i]) {
                dfs(i, computers, visited); // 재귀 호출
            }
        }
    }
}