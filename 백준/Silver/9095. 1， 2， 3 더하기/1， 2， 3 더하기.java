import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{
	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int t = Integer.parseInt(st.nextToken());
		
		for(int tc =0; tc<t;tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			
			System.out.println(dfs(N));
		}//tc
	}

	public static int dfs(int n) {
		if(n== 1 || n== 2) return n;
		else if(n==3) return 4;
		
		return dfs(n-1)+dfs(n-2)+dfs(n-3);
	}
}
