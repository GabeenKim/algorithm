import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st =new StringTokenizer(br.readLine());
		
		//배열좌표는 1부터 입력되니까 0~100말고 1~101 => 100이라는 좌표가 나올 수 있으니
		int[][] arr = new int[101][101];

		int num = Integer.parseInt(st.nextToken());
		for(int n = 0; n<num; n++) {
			st = new StringTokenizer(br.readLine()," ");
			int si = Integer.parseInt(st.nextToken());
			int sj = Integer.parseInt(st.nextToken());
		
			for(int i=si; i<si+10; i++) {
				for (int j =sj; j<sj+10 ; j++) {
					if (arr[i][j] == 0) 
						arr[i][j] = 1;
				}
			}
		}

		int cnt = 0;
		for(int i=1;i<101;i++) {
			for(int j=1;j<101;j++) {
				if (arr[i][j] ==1 ) {
					if(arr[i-1][j]==0) cnt++;
					if(arr[i+1][j]==0) cnt++;
					if(arr[i][j-1]==0) cnt++;
					if(arr[i][j+1]==0) cnt++;
				}
			}
		}
		System.out.println(cnt);

	}

}
