import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        Stack<String> stackStr = new Stack<>();
        int[] Array = new int[2];
        int cnt=0;
        int check=0;
        for (int i=0; i<words.length; i++){
            if (stackStr.isEmpty()) {
                stackStr.push(words[i]);
                cnt ++;
            }
            else{
                if (stackStr.contains(words[i])){
                    cnt++;
                    check++;
                    break;
                }
                else if(!(stackStr.contains(words[i])) && stackStr.peek().charAt(stackStr.peek().length()-1) != words[i].charAt(0)){
                    cnt ++;
                    check++;
                    break;
                }
                else{
                    cnt++;
                    stackStr.push(words[i]);
                }
            }
        }
        if (check!=0){
            if (cnt % n == 0){
                Array[0] = n;
                Array[1] = (int)cnt/n;       
            }
            else{
                Array[0] = cnt%n;
                Array[1] = (int)cnt/n+1;
            }
            
        }
        else {
            Array[0] = 0;
            Array[1] = 0;
        }
        return Array;
    }
}
