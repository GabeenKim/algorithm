import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		int[] dp = new int[N];
		int maxNum = 0;

		st = new StringTokenizer(br.readLine()," ");
		for(int n=0; n<N;n++) {
			arr[n]= Integer.parseInt(st.nextToken());
		}
		//dp와 maxNum 초기화
		dp[0]=arr[0];
		maxNum = arr[0];

		for(int i=1; i<N;i++) {
			dp[i] = Math.max(dp[i-1]+arr[i] , arr[i]);
			maxNum = Math.max(maxNum, dp[i]);	 
		}

		System.out.println(maxNum);
	}

}