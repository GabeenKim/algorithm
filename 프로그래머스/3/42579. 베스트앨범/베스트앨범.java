import java.util.*;

class Solution {
    public List<Integer> solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        Map<String,Integer> hm = new HashMap<>();
        for(int i=0; i<genres.length;i++){
            hm.put(genres[i],hm.getOrDefault(genres[i],0)+plays[i]);
        }
        //내림차순 정렬
        List<String> keySet = new ArrayList<>(hm.keySet());
        keySet.sort((o1, o2) -> hm.get(o2) - hm.get(o1));
        
        //재생 수와 고유번호 엮기 
        int[][] arr = new int[plays.length][2];
        for(int i=0; i<plays.length; i++){
            arr[i][0] = plays[i];
            arr[i][1] = i;
        }
        
        //재생 수 내림차순 정렬 
        Arrays.sort(arr,(o1,o2)-> o2[0] - o1[0]);
        
        int count=0;
        for(String key : keySet){
            for(int i=0;i<arr.length ;i++){
                if(genres[arr[i][1]].equals(key)){
                    if(count <2){
                        answer.add(arr[i][1]);
                        count++;
                    }
                    else break;
                }
            }
            if(count==2 || count==1) count=0;
        }
        
        return answer;
    }
}