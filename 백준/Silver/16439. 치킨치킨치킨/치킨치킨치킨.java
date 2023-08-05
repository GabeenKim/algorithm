import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N,M,max;
	static int[][] arr;
	static int[] col;
	static boolean[] v;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		col = new int[3];
		v= new boolean[M];
		
		for(int i=0; i<N;i++) {
			st = new StringTokenizer(br.readLine()," ");
			for (int j=0; j<M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		max = 0; 
		combi(0,0);
		System.out.println(max);
	}
	//M개 중에서 3개 뽑기 
	public static void combi(int cnt, int start) {
		if(cnt==3) {
			int result =0;
			//주어진 조합에 대해서 0~N-1행까지의 최대 만족도
			for(int i=0;i<N;i++) {
				int likes = 0;
				for(int j : col) {
					likes = Math.max(likes, arr[i][j]);
				}
				//주어진 조합들을 다 
				result += likes;
			}
			if(result>max)max=result;
			return;
		}
		
		for (int j=start; j<M; j++) {
			//	중복체크 후 사용하지 않았다면 선택
			if(v[j]) continue;	// 사용했다면 다음번호로..

			v[j]=true;
			col[cnt]=j;
			combi(cnt+1,j+1);
			v[j]=false;
		}
	}
	
	
	public static void dfs(int i,int likes) {
		if(i==N) {
			if(likes>max) max= likes;
			return;
		}
		for(int j : col) {
				dfs(i+1,likes+arr[i][j]);
		}
	}
}
