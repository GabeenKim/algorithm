import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N,cnt;
	static int[][] arr, score;
	static int[] ans; 
	static boolean[] v;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N= Integer.parseInt(st.nextToken());
		
		arr= new int[N][3];
		ans = new int[3];
		v = new boolean[10];
		score = new int[N][2];
		
		for(int i=0;i<N;i++) {
			String input = br.readLine();
			for(int j=0; j<3;j++) {
				arr[i][j] = input.charAt(j)-'0';
			}
			score[i][0] = input.charAt(4)-'0';
			score[i][1] = input.charAt(6)-'0';
		}

		dfs(0);
		System.out.println(cnt);
	}
	public static void dfs(int n) {
		if(n==3) {
			//정답처리-> 1~9까지의 수 3개를 고른 상황. 
			//따라서 내가 생각한 수열 ans이 질문 조건에 해당하는지 점검 
			int check=0;
			for(int i=0;i<N;i++) {
				int strike=0, ball=0;
				for(int j=0; j<3;j++) {
					//인덱스가 j로 같고 값이 동일하다면 스트라이크
					if(arr[i][j]==ans[j]) {
						strike++;
					}
					else {
						for(int num:arr[i]) {
							if(num == ans[j])ball++;
						}
					}
				}
				if(score[i][0]==strike && score[i][1]==ball)
					check++;
			}//반복문
			if(check==N) cnt++;
			return;
		}
		//[2]하부 함수 호출(1~9 까지)
		// 순서 상관 있고, 중복 허용 X 따라서 순열 이용.
		for(int i=1;i<=9;i++) {
			//중복 체크 
			if(v[i]) continue;
			v[i]= true;
			//현재 ans에서 n위치에 1~9 중 고른 값 넣고
			ans[n]=i;
			//다음 재귀 탐색하기 
			dfs(n+1);
			
			//중복 해제 -> 원래대로
			v[i] = false;
		}
	}
}
