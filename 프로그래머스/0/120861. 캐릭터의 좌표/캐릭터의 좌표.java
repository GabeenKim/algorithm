class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[2];
        int xSize = board[0]/2, ySize = board[1]/2 ;
        int x = 0, y = 0;
        
        for(int i=0 ; i< keyinput.length ;i++){
            int nx = x, ny = y; 
            
            if(keyinput[i].equals("left")) nx--;
            else if(keyinput[i].equals("right")) nx++; 
            else if(keyinput[i].equals("up")) ny++;
            else if(keyinput[i].equals("down")) ny--;
        
            //실행, 조건검사 후 값 변경해야지, 조건 먼저 검사하고 실행하면 답이 이상하게 나옴;;
            if(Math.abs(nx) <= xSize && Math.abs(ny) <= ySize) {
                x = nx;
                y = ny;
            }
        
        }
        
        answer[0] = x; 
        answer[1] = y;
        
        return answer;
    }
}