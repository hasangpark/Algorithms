# import sys
# sys.setrecursionlimit(10**7)
def solution(places):
    answer = []
    for p in places:
        array = []
        for y in range(5):
            for x in range(5):
                if p[y][x] == 'P':
                    visited = [[False] * 5 for _ in range(5)]
                    visited[y][x] = True
                    dfs((x, y), (x, y-1), p, visited, array, 1)
                    dfs((x, y), (x, y+1), p, visited, array, 1)
                    dfs((x, y), (x-1, y), p, visited, array, 1)
                    dfs((x, y), (x+1, y), p, visited, array, 1)
        if len(array) > 0:
            answer.append(0)
        else:
            answer.append(1)
    return answer

def dfs(pos1, pos2, p, visited, array, step):
    x, y = pos2[0], pos2[1]
    if not(0 <= x < 5) or not(0 <= y < 5) or visited[y][x] or step > 2 or p[y][x] == 'X':
        return
    if p[y][x] == 'P':
        return array.append(pos1)
    dfs((x, y), (x, y-1), p, visited, array, step + 1)
    dfs((x, y), (x, y+1), p, visited, array, step + 1)
    dfs((x, y), (x-1, y), p, visited, array, step + 1)
    dfs((x, y), (x+1, y), p, visited, array, step + 1)
