
n,m,r = map(int, input().split())

adj = [[] for _ in range(n+3)]
visited = [False for _ in range(n+3)]
answer = [0 for _ in range(n+3)]
idx = 1
def dfs1(cur):
    global idx
    visited[cur] = True
    answer[cur] = idx
    idx += 1
    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs1(nxt)

def dfs2():
    S = []
    S.append(r)
    while S:
        cur = S.pop()
        visited[cur] = True
        for nxt in adj[cur]:
            if not visited[nxt]:
                S.append(nxt)

for i in range(m):
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1,n+1):
    adj[i].sort()

dfs1(r)

for i in range(1,n+1):
    print(answer[i])