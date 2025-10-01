//소인수분해는 n의 제곱근까지만 구하면 됨,,, 바부,,,
import java.util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        int[] answer = {};
        
        for(int i=2; i*i<=n; i++){
            while (n%i==0) {
                n/=i;
                list.add(i);
            } 
        }
        
        if(n > 1) list.add(n); //제곱근 이하에서 떨어지지 않을 경우 자기 자신이 소수.
        
        answer = list.stream().distinct().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}