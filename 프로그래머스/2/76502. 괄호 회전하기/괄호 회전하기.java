import java.util.*;

class Solution {
    public int solution(String s) {
        int answer=0;
        
        for(int i =0; i<s.length(); i++){
            String rotatedS = s.substring(i) + s.substring(0,i);
            if(isValid(rotatedS)) answer++;
        }
        
        return answer;
    }
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                
                char open = stack.pop();
                if ((open == '(' && ch != ')') ||
                    (open == '{' && ch != '}') ||
                    (open == '[' && ch != ']')) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}