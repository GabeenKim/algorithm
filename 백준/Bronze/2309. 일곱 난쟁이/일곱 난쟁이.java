
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] arr,ans;
	static boolean stop = false;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		arr= new int[9];
		ans = new int [9];
		for(int i=0; i<9;i++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			arr[i]=N;
		}
		
		dfs(0,0,0);
	}
	public static void dfs(int n, int count, int height) {
		if(stop)return;
		if(n==9) {
			if(count==7 && height==100){
				//정답처리
				Arrays.sort(ans);
				for(int num : ans) {
					if(num==0) continue;
					System.out.println(num);
				}
				stop = true;
			}
			return;
		}
		ans[n]=arr[n];
		dfs(n+1,count+1,height+arr[n]);
		ans[n]=0;
		dfs(n+1,count,height);
	}
}
