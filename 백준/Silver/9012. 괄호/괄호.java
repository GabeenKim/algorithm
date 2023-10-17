import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());
		
		for(int t=0;t<T;t++) {
			st = new StringTokenizer(br.readLine());
			String str = st.nextToken();
			
			Stack<String> stack = new Stack<>();
			
			int i=0;
			for(i=0;i<str.length();i++) {
				char ch = str.charAt(i);
				String strCh = String.valueOf(ch);
				
				if(i==0 && strCh.equals(")")) {
					System.out.println("NO");
					break;
				}
				else if(strCh.equals(")")) {
					if(!stack.isEmpty() && stack.peek().equals("(")) stack.pop();
					else stack.push(strCh);
				}
				else if(strCh.equals("(")){
					stack.push(strCh);
				}	
			}//for
			if(i == 0) continue;
			if (stack.isEmpty()) System.out.println("YES");
			else System.out.println("NO");
				
		}
	}
}
