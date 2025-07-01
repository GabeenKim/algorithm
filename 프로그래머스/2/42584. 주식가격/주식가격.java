import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Queue<Integer> queue = new LinkedList<>();
        for(int n : prices) queue.offer(n);
        
        int index = 0;
        while(!queue.isEmpty()){
            int target = queue.poll();
            for(int q:queue){
                answer[index]++;
                if(target>q) break;
            }
            index++;
        }
        return answer;
    }
}