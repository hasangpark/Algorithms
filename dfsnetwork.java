class Solution {
    public int solution(int n, int[][] computers) {
        
        boolean[] visited = new boolean[n];
        int answer=0;
        for(int i=0; i<n;i++){
            if (!visited[i]) {
                dfs(computers,i,visited);
                answer++;
                    
            }
        }
        return answer;
    }
    
    public void dfs(int[][] computers, int node, boolean[] visited){
        visited[node] = true;
        for(int i=0; i<computers.length;i++){
            if (computers[node][i] ==1 && !visited[i]){
                dfs(computers, i, visited);
            }
        }
    }
}
