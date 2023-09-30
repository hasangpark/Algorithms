import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<String> hs01 = new HashSet<String>();
        for(int i=0; i<nums.length;i++){
        hs01.add(Integer.toString(nums[i]));
        }
        for(String e:hs01){
            answer ++;
            if(answer==(int)nums.length/2){
                break;
            }
        }
        return answer;
    }
}
