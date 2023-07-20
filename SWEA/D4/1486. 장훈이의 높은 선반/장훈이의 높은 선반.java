import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N,B,ans;
	static int[] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int TC = Integer.parseInt(br.readLine());
		
		for(int tc=1;tc<=TC;tc++) {
			st = new StringTokenizer(br.readLine()," ");
			
			N = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			
			arr = new int[N];
			
			st = new StringTokenizer(br.readLine()," ");
			for(int i=0;i<N;i++) arr[i] = Integer.parseInt(st.nextToken());
			
			ans = 10000*N;
			dfs(0,0);
			System.out.println("#"+tc+" "+ans);
		}
	}
	public static void dfs(int n,int sum) {
		if(n==N) {
			if(sum>=B) {
				if(sum-B<ans) ans = sum-B;
			}
			return;
		}
		//선택 
		dfs(n+1,sum+arr[n]);
		//미선택
		dfs(n+1,sum);
	}
}
