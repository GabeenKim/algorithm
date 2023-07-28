import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		Queue<Integer> q = new LinkedList<>();
		StringBuilder ans= new StringBuilder();
		ans.append("<");
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		for(int n=1; n<=N; n++) q.add(n);
		
		while(q.size()>0) {
			for(int i=0;i<K-1;i++) {
				q.add(q.poll());
			}
			ans.append(q.poll()).append(", ");
		}
		for(int i : q) {
			ans.append(i).append(", ");
		}
		ans.delete(ans.length()-2, ans.length());
		ans.append(">");
		System.out.println(ans);	
	}

}
