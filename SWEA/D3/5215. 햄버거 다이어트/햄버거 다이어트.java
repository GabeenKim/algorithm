import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int N,L,max;
	static int[][] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1;t<=T;t++) {
			st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			arr = new int[N][2];
			max = 0;
			for(int n=0;n<N;n++) {
				st = new StringTokenizer(br.readLine(), " ");
				arr[n][0] = Integer.parseInt(st.nextToken());
				arr[n][1] = Integer.parseInt(st.nextToken());
			}
			
			//뽑을 것의 인덱스, 점수 T, 칼로리 K의 초기값
			dfs(0,0,0);
			
			System.out.println("#"+t+" "+max);
		}//테스트케이스
	}
	
	public static void dfs(int n, int T, int K) {
		//종료조건
		if(n==N) {
			//정답처리
			if(K<=L && T>max) {
				max = T;
			}
			return;
		}
		//하부 함수 호출
		//해당 인덱스를 선택한 경우
		dfs(n+1,T+arr[n][0],K+arr[n][1]);
		//인덱스 선택 X한 경우
		dfs(n+1,T,K);
	}
}
