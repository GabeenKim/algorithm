import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;


public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char arr[] = br.readLine().toCharArray();
		Stack<Character> st = new Stack<>(); 
		
		int ans = 0; 
		int cost = 1;
		
		for(int i=0; i<arr.length;i++) {
			char c = arr[i];
			if(c=='(' || c=='[') {
				st.push(c);
				cost *= (c=='('? 2 : 3); 
			}
			else {
				if(st.isEmpty()) {
					ans=0; 
					break;
				}
				else {
					if(c==')') {
						if(arr[i-1]=='(')
							ans += cost;
						cost /=2;
						if(st.peek()=='(')
							st.pop();
					}
					else if(c==']') {
						if(arr[i-1]=='[')
							ans+=cost;
						cost/=3;
						if(st.peek()=='[')
							st.pop();
					}
				}
			}
			
		}
		if(!st.isEmpty()) ans=0;
		
		System.out.println(ans);	
		
	}
}
