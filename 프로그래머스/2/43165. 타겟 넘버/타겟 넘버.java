class Solution {
    int answer =0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0,0,target);
    
        return answer;
    }
    
    public void dfs(int[] numbers, int depth, int sum, int target){
        //마지막 노드까지 탐색한 경우
        if(depth == numbers.length){
            if(target == sum) answer++ ;
            return;
        }
        int plus = sum + numbers[depth];
        int minus = sum - numbers[depth];
        
        dfs(numbers,depth+1, plus, target);
        dfs(numbers, depth+1, minus, target);
    }
}