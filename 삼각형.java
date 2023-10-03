import java.util.*;
class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        Arrays.sort(sides);
        
        //가장 긴 변의 길이가 새로 정해지는경우
        for(int i=sides[1];i<sides[1]+sides[0]; i++) answer+=1;
        //가장 긴 변의 길이가 두 번째 수인 경우
        //위에서 중복된 경우를 계산해줬으니 이번 경우에서는 그 경우 제외 세변의 길이가 다 같을수도 있잖아?
        for(int i=sides[1]-1; i+sides[0]>sides[1];i--) answer+=1;
        return answer;
    }
}
