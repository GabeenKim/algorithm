import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int end =0;
        int index =0;
        int cnt =0; //작업 끝난 시간, 인덱스, 수행 요청 개수
        
        //요청 시점 별 정렬
        Arrays.sort(jobs,(o1,o2)->o1[0] - o2[0]);
        //소요 시간이 짧은 작업부터 우선순위 주는 우선순위 큐 
        PriorityQueue<int[]> que = new PriorityQueue<>((o1,o2)->o1[1]-o2[1]);
        
        //요청이 모두 수행될 때까지
        while(cnt< jobs.length){
            //한 작업이 완료되는 시점까지 들어온 모든 요청을 큐에 넣기
            while(index <jobs.length && jobs[index][0] <= end){
                que.add(jobs[index++]);
            }
            if(que.isEmpty()){
                end = jobs[index][0];
            }
            else{
                int[] tmp = que.poll();
                
                answer += tmp[1] + end - tmp[0];
                end += tmp[1];
                cnt++;
            }
            
        }
        
        
        return answer/jobs.length;
    }
}