import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        
        int[][] dp = new int[triangle.length][triangle.length];

        dp[0][0] = triangle[0][0];
     
        
        // 윗줄부터 한 칸씩 내려오면서 DP 테이블을 채웁니다.
        for (int i = 1; i < triangle.length; i++) {
            // 가장 왼쪽 칸 (j=0)일 때 
            dp[i][0] = dp[i - 1][0] + triangle[i][0];

            // 중간 칸 점화식 : dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            for (int j = 1; j < i; j++) {
                dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
            }
            // 가장 오른쪽 칸 (j=i)
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i];
        }
        
        // 마지막 층에서 최댓값을 찾습니다.
        for (int i = 0; i < triangle[triangle.length - 1].length; i++) {
            answer = Math.max(answer, dp[triangle.length - 1][i]);
        }
        
        return answer;
    }
}