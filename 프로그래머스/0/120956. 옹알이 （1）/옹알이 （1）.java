class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] arr = { "aya", "ye", "woo", "ma"};
        
        for(String str : babbling){
            for(int i=0; i<arr.length; i++){
                 str = str.replace(arr[i]," ");
             }
            if(str.trim().length()==0) answer++;
        }
        return answer;
    }
}