import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> queue = new LinkedList<>();
        int cnt = 0, idx = 0, curWeight = 0;  
        
        for(int i=0; i<bridge_length; i++) queue.offer(0);
        
        while(idx < truck_weights.length){
            curWeight -= queue.poll();
            cnt++;
            if(curWeight + truck_weights[idx] <= weight){
                curWeight += truck_weights[idx];
                queue.offer(truck_weights[idx++]);
            }
            else queue.offer(0);
        }
        return cnt+bridge_length;
        
    }
}