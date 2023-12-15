import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int cnt = 0;
        
        for(int num : priorities) 
            pq.offer(num);
    
        while(!pq.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if(pq.peek() == priorities[i]){
                    cnt++;
                    pq.poll();
                    if(i== location)
                        return cnt;
                }
            }
        }
    return cnt;
    }
}

