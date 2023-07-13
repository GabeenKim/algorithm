
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		//구간합 저장 배열
		int[] arr = new int[N+1];
		
		st = new StringTokenizer(br.readLine()," ");
		for(int n=1;n<N+1;n++)
			arr[n]=arr[n-1]+Integer.parseInt(st.nextToken());
		
		for(int m=0;m<M;m++) {
			st = new StringTokenizer(br.readLine()," ");
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			
			System.out.println(arr[j]-arr[i-1]);
		}
	}

}
