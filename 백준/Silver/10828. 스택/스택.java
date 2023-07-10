import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		Stack<Integer> stack = new Stack<>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());

		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine(), " ");
			String command = st.nextToken();
			
			switch(command) {
			case "push" :
				int num = Integer.parseInt(st.nextToken());
				stack.push(num);
				break;
			case "pop" :
				if(stack.empty()) System.out.println(-1); 
				else System.out.println(stack.pop());
				break;
			case "size" :
				System.out.println(stack.size()); 
				break;
			case "empty" :
				if(stack.empty())System.out.println(1);
				else System.out.println(0);
				break;
			default :
				if(stack.empty()) System.out.println(-1); 
				else System.out.println(stack.peek()); 
				break;
			}
			
		}
	}

}
