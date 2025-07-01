import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int[][] arr = new int[102][102];
		
		for(int n=0; n<N; n++) {
			st = new StringTokenizer(br.readLine()," ");
			int si = Integer.parseInt(st.nextToken());
			int sj = Integer.parseInt(st.nextToken());
			
			//입력 받은 영역을 1로 채우기 
			for(int i=si; i<si+10;i++) {
				for(int j=sj; j<sj+10; j++) {
					arr[i][j]=1;
				}
			}
			
		}
		
		int ans = 0;
		int[] di = {-1,1,0,0};
		int[] dj = {0,0,-1,1};
		//4방향을 확인하고, 현재가 1일 때 다른 방향이 0이면 그 부분이 둘레임을 이용
		for(int i=1;i<=100;i++) {
			for(int j=1;j<=100;j++) {
				if(arr[i][j]==1) {
					for(int k=0;k<4;k++) {
						int ni = i+ di[k];
						int nj = j + dj[k];
						
						if(arr[ni][nj]==0) ans++;
					}
				}
			}
		}
		System.out.println(ans);
		
	}
}
