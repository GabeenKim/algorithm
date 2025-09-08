class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int[] di = {-1,1,0,0,-1,-1,1,1};
        int[] dj = {0,0,-1,1,-1,1,-1,1};
        
        for(int i=0; i<board.length;i++){
            for(int j=0; j<board.length; j++){
                if(board[i][j]==1){
                    for(int d=0; d<8;d++){
                        int ni = i+di[d];
                        int nj = j+dj[d];
                        if(ni>=0 && ni<board.length && nj>=0 &&nj<board.length
                           && board[ni][nj]==0) 
                            board[ni][nj]=2;
                    }
                }
            }
        }
        for(int i=0; i<board.length;i++){
            for(int j=0; j<board.length; j++){
                if(board[i][j]==0) answer++;
            }
        }
        return answer;
    }
}