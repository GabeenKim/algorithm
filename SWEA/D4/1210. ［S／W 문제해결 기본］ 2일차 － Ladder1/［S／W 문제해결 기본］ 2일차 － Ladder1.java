import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int TC = 10;
		for(int tc=1; tc<=TC; tc++) {
			st = new StringTokenizer(br.readLine());
			int T = Integer.parseInt(st.nextToken());
			
			int[][] arr = new int[100][102];
			
			for(int i=0;i<100;i++) {
				st = new StringTokenizer(br.readLine()," ");
				for(int j=1;j<=100;j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int ci = 99, cj = 1;
			for(cj=1;cj<=100;cj++) {
				if(arr[ci][cj]==2) break;
			}
			
			while(ci>0) {
				arr[ci][cj] = 0 ;
				if(arr[ci][cj-1]==1) cj--;
				else if(arr[ci][cj+1]==1) cj++;
				else ci--;
			}
			System.out.println("#"+T+" "+(cj-1)+"\n");
			
		}
	}

}
