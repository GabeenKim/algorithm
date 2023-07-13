
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st ;

		int[][] arr = new int[100][102];
		
		for(int tc = 1; tc<=10;tc++){
			int TC = Integer.parseInt(br.readLine());
			//배열 입력
			for(int i=0;i<100;i++) {
				st = new StringTokenizer(br.readLine()," ");
				for(int j=1;j<=100;j++){
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int si=99, sj = 1;
			for(int j=1;j<=100;j++) {
				if(arr[99][j]==2) {
					sj = j; 
					break;
				}
			}
			
			
			while(si>0) {
				arr[si][sj]=0;
				if(arr[si][sj-1]==1) sj--;
				else if(arr[si][sj+1]==1) sj++;
				else si--;
			}
			//여유공간 만들어준 것. 오른쪽에
			System.out.print("#"+tc+" "+(sj-1)+"\n");
		}

	}

}
