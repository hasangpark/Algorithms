import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<String> stack = new Stack<>();
        System.out.println("Hello Java");
        for(int i=0; i<s.length(); i++){
            if (stack.isEmpty()) stack.push(s.substring(i,i+1));
            else{
                if (s.charAt(i) =='(') stack.push(s.substring(i,i+1));
                else{stack.pop();}
            }
        }

        return stack.isEmpty();
    }
}
