import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		Stack<Integer> stack = new Stack<>();
		Stack<Integer> index = new Stack<>();
		
		st = new StringTokenizer(br.readLine());
		for(int i=1; i<=N;i++) {
			int input= Integer.parseInt(st.nextToken());
			
			while(!stack.isEmpty()) {
				if(stack.peek()>input) {
					System.out.print(index.peek()+" ");
					stack.push(input);
					index.push(i);
					break;
				}
				else {
					stack.pop();
					index.pop();
				}
			}
			if(stack.isEmpty()) {
				System.out.print(0+" ");
				stack.push(input);
				index.push(i);
			}
		}
	}
}
