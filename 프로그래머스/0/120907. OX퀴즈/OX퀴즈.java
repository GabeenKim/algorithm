import java.util.*;
class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for(int i=0; i< quiz.length; i++){
            String[] str = quiz[i].split(" ");
            
            int X = Integer.parseInt(str[0]);
            int Y = Integer.parseInt(str[2]);
            int Z = Integer.parseInt(str[4]);
            System.out.println(X+" "+Y+" "+Z);
            
            if(str[1].equals("-")){
                if(X-Y==Z) answer[i]="O";
                else answer[i]="X";
            }else{
                if(X+Y==Z) answer[i]="O";
                else answer[i]="X";
            }
        }
        
        return answer;
    }
}