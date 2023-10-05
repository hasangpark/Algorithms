import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        HashMap<Double, Integer> map = new HashMap<>();
        int[] result = new int[score.length];

        for (int i = 0; i < score.length; i++) {
            double tmp = (score[i][0] + score[i][1]) / 2.0;
            int rank = score.length;

            for (int j = 0; j < score.length; j++) {
                if (i != j) {
                    if (tmp > (score[j][0] + score[j][1]) / 2.0) {
                        rank--;
                    } else if (tmp == (score[j][0] + score[j][1]) / 2.0) {
                        rank--;
                    }
                }
            }

            if (!map.containsKey(tmp)) {
                map.put(tmp, rank);
            }
        }

        for (int i = 0; i < score.length; i++) {
            result[i] = map.get((score[i][0] + score[i][1]) / 2.0);
        }

        return result;
    }
}
