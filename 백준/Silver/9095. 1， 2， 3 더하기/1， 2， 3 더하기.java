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

	public static int dfs(int n) {
		if(n<3) return n;
		if(n==3) return 4;
		
		dp[1]=1; dp[2]=2; dp[3]=4;
		for(int i=4;i<=n;i++) {
			dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
		}
		return dp[n];
	}
}
