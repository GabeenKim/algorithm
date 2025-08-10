import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long start = 1;
        long end =(long) n* times[times.length-1]; // 가장 오래 걸리는 심사관이 n명을 모두 심사하는 경우
        long answer = end; //초기 값은 최대값으로 설정 
        
        //이진 탐색
        while(start<=end){
            long mid = (start + end) / 2; //mid는 현재 가정하는 총 걸리는 시간 
            long people = 0; //mid시간 동안 처리 할 수 있는 인원
            //mid 시간 동안 각 심사관이 처리할 수 있는 인원 계산
            for(int time : times){
                people += mid/time;
                //n명 이상이면 이미 충분 하므로 계산할 필요 없음.
                if(people >=n) break;
            }
            
            if(people >= n ){
                //mid 시간 안에 n 명 이상 처리가 가능하면 더 줄여본다
                answer = mid;
                end = mid-1;
            }else{
                //mid 시간으로는 부족하다면 시간을 늘려본다
                start = mid+1;
            }
        }
        
        return answer;
    }
}