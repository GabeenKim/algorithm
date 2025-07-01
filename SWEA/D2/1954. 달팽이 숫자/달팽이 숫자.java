import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int tc = Integer.parseInt(st.nextToken());
		for(int t=1;t<=tc;t++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			
			int[][] arr = new int[n][n];
			int[] di = {0,1,0,-1}; //우, 하, 좌, 상
			int[] dj = {1,0,-1,0};
			
			int i=0, j=0,dr=0;
			for(int cnt=1; cnt<=n*n;cnt++) {
				arr[i][j] = cnt;
				
				int ni = i+di[dr];
				int nj = j+dj[dr];
				
				if(0<=ni && ni<n && 0<=nj && nj<n && arr[ni][nj]==0) {
					i= ni; j= nj;
				}else {
					dr=(dr+1)%4; //0,1,2,3 반복 
					i= i+di[dr];
					j = j+dj[dr];
				}
			}
			System.out.println("#"+t);
			for(int[] lst: arr) {
				for(int num:lst) {
					System.out.print(num+" ");
				}
				System.out.println();
			}
		}
	}

}
