import java.util.*;

class Solution {
    public int[] solution(long n) {
        String str = n+"";
        String[] strArr = str.split("");
        int[] answer = new int[strArr.length];
        int idx = 0;
        
        for(int i=strArr.length-1; i>=0 ; i--){
            answer[i] = Integer.parseInt(strArr[idx++]);
        }
        return answer;
    }
}