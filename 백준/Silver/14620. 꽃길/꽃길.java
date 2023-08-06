import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N,ans,cnt;
	static int[][] arr;
	static boolean[][] v;
	static int[] di = {-1,1,0,0};
	static int[] dj = {0,0,-1,1};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		arr = new int[N][N];
		v = new boolean[N][N];
		
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine()," ");
			for(int j=0;j<N;j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		cnt = 0;
		ans = 200*5*3;
		dfs(0,0);
		System.out.println(ans);
	}
	public static void dfs(int cnt, int costSum) {
		if(cnt==3) {
			ans = Math.min(ans, costSum);
			return;
		}
		//씨앗을 1행1열부터 심어야 경계에 안 걸치고 꽃잎 존재 가능
		for(int i=1;i<N-1;i++) {
			for(int j=1;j<N-1;j++) {
				//화단을 벗어나는지 아닌지 체크 
				boolean find = true;
				int cost=0;
				if(!v[i][j]) cost+=arr[i][j];
				for(int k=0;k<4;k++) {
					int ni = i+di[k];
					int nj = j+dj[k];
					//1.범위 내, 2. 미방문 확인 
					if (ni<0 || nj<0 || ni>=N || nj>=N || v[ni][nj]) {
						find = false;
						break;
					}
					cost += arr[ni][nj];
				}	
				//4방면이 다 안 벗어나고 비어있다면 4지점 다 체크
				if(find) {
					v[i][j] = true;
					for(int n = 0; n < 4; n++) {
						v[i][j] = true;
						int ni = i + di[n];
						int nj = j + dj[n];
						
						v[ni][nj] = true;
						
					}
					dfs(cnt+1,costSum+cost);
					//4지점 다 해제
					for(int n = 0; n < 4; n++) {
						v[i][j] = false;
						int ni = i + di[n];
						int nj = j + dj[n];
						
						v[ni][nj] = false;
					}
					v[i][j] = false;
				}
				
			}
		}
	}
}
