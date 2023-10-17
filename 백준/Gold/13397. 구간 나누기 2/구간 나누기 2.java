import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] arr ;
	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		arr = new int[N];
		
		int maxNum = 0;
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N ; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			maxNum = Math.max(maxNum, arr[i]);
		}
		
		int left = 0, right = maxNum;
		//left>=right면 탈출
		while(left<right) {
			int mid = ( left+right )/2;
			//구간의 개수가 M이하여야 하므로 개수가 많으면 right를 줄여서 다시 탐색
			if(solve(mid)<=M) {
				right = mid;
			}
			else {
				left = mid+1;
			}
		}
		
		System.out.println(right);
		
	}
	public static int solve(int mid) {
		int cnt =1;
		int min = 10000+1;
		int max = 0;
		
		for(int i=0; i<N;i++) {
			min = Math.min(min, arr[i]);
			max = Math.max(max, arr[i]);
			
			if(max-min >mid) {
				cnt ++;
				min = 10000+1; max = 0;
				i--;
			}
		}
		return cnt; //mid보다 큰 최댓값이 포함된 구간의 수 
	}
}
