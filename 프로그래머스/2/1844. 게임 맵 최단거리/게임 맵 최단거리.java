import java.util.*;
class Solution { 
    static int[] di ={1,-1,0,0};
    static int[] dj = {0,0,-1,1};
    
    static class Pos{
        int i, j, cnt;
        public Pos(int i, int j, int cnt){
            this.i = i;
            this.j = j;
            this.cnt = cnt;
        }
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length; 
        int m = maps[0].length;
        
        boolean[][] visited = new boolean[n][m];
        Queue<Pos> queue = new LinkedList<>();
        queue.add(new Pos(0,0,0)); //세로,가로,이동횟수
        visited[0][0] = true;
        
        while(!queue.isEmpty()){
            Pos c = queue.poll();
            if(c.i==n-1 && c.j==m-1) {
                answer = c.cnt;
                break;
            }
            
            for(int d=0;d<di.length;d++){
                int ni = c.i + di[d];
                int nj = c.j + dj[d];
                
                if(ni>=0 && ni<n && nj>=0 && nj<m){
                    if(maps[ni][nj] ==1 && !visited[ni][nj]){
                        visited[ni][nj] = true;
                        queue.add(new Pos(ni,nj,c.cnt+1));
                    }
                }
            }
        }
        if(answer == 0) {
            answer = -1;
        }else{
            answer+=1;
        }
        
    
        return answer;
    }
}