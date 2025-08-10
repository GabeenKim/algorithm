import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Queue<Integer> queue = new PriorityQueue<>();
        
        for(int i=0; i<scoville.length;i++){
            queue.add(scoville[i]);
        }
        
        //모든 음식의 스코빌 지수가 K이상이 되면 끝
        while(queue.peek()<K){
            //큐에 음식이 하나만 남았다면 더 이상 섞을 음식이 없음. 
            if(queue.size()==1) return -1; 
            
            queue.add(queue.poll()+(queue.poll()*2));
            answer++;
        }
        
        return answer;
    }
}