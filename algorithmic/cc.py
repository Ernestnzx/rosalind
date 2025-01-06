with open('./testcase/rosalind_cc.txt','r') as f:
    n,m = map(int,f.readline().split())
    al,vis = [[] for _ in range(n)], [0]*n
    for line in f.readlines():
        u,v = map(int,line.split());u-=1;v-=1;
        al[u].append(v)
        al[v].append(u)
def dfs(u):
    global vis,al
    vis[u] = 1
    for v in al[u]:
        if not vis[v]:
            dfs(v)
ans = 0
for u in range(n):
    if not vis[u]:
        dfs(u); ans+=1
print(ans)
