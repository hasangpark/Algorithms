class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int garo = 0;
        int sero = 0;
        
        for(int i=0; i<sizes.length; i++){
            if (sizes[i][0]>=sizes[i][1]){
                continue;
            }
            else{
                int a = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = a;
            }
        }
        for (int i=0; i<sizes.length;i++){
            if (garo<=sizes[i][0]){
                garo = sizes[i][0];
            }
            if (sero<=sizes[i][1]){
                sero = sizes[i][1];
            }
        }
        
        return garo*sero;
    }
}
