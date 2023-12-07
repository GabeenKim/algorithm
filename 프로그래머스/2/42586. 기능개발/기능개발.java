import java.util.*;
class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        int count = 1;
        
        for(int i=0; i<progresses.length;i++){
            int date = (int)(Math.ceil((100.0-progresses[i])/speeds[i]));
            queue.add(date);
        }
        
        int preWork = queue.poll();
        while(!queue.isEmpty()){
            if(preWork >= queue.peek()){
                count ++;
                queue.poll();
               
            }else if(preWork < queue.peek()){
                answer.add(count);
                count=1;
                preWork = queue.poll();
            }
        }
        answer.add(count);
      
        return answer;
    }
}