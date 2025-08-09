import java.util.*;

class Solution {
    public int solution(int N, int number) {
        //N이 number일 때는 N밖에 답이 없음.
        if(N == number) return 1;
        
        Set<Integer>[] dp = new HashSet[9];
        for(int i=0; i <= 8; i++){
            dp[i] = new HashSet<>();
        }
        
        //dp[i]는 N을 i번 사용하여 만들 수 있는 집합.
        //우선 N을 i번 이어 붙였을 때 만들 수 있는 수를 넣어 dp[i]초기화
        for(int i=1; i <= 8; i++){
            dp[i].add(Integer.parseInt(String.valueOf(N).repeat(i)));
        }
        
        //N을 j번 사용한 결과(dp[j])와 N을 i-j번 사용한 결과(dp[i−j])를 사칙연산한 것.
        for (int i = 2; i <= 8; i++) {
            for(int j=1; j < i; j++){
                Set<Integer> set1 = dp[j];
                Set<Integer> set2 = dp[i-j];

                for(int num1 : set1){
                    for(int num2 : set2){
                        dp[i].add(num1+num2);
                        dp[i].add(num1-num2);
                        dp[i].add(num1*num2);
                        if(num2!=0)
                            dp[i].add(num1/num2);
                    }
                }
            }
            if (dp[i].contains(number)) {
                    return i;
                }
        }
        
        return -1;
    }
}