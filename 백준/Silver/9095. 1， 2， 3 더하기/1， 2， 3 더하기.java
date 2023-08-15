import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] dp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int t = Integer.parseInt(st.nextToken());
		
		for(int tc =0; tc<t;tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			
			dp = new int[N+1];
			
			System.out.println(dfs(N));
		}//tc
	}

	/*
	 	1,2,3의 합으로 N을 이루는 개수는 다음의 규칙을 따른다. 단, n>=4인 경우에만 
	 	N = N-1번째의 경우의 수 + N-2번째의 경우의 수 + N-3번째의 경우의 수 
	 */
	public static int dfs(int n) {
		//n<3인 경우 초기값으로 다음과 같이 주어짐. 
		if(n== 1 || n== 2) return dp[n]=n;
		else if(n==3) return dp[n]=4;
		
		if(dp[n]!=0) return dp[n];
		else {
			//n>=4이고 dp 테이블에 값이 없는 경우 재귀탐색 실행
			return dp[n]=dfs(n-1)+dfs(n-2)+dfs(n-3);
		}
	}
}
