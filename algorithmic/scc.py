with open('./testcase/rosalind_scc.txt','r') as f:
    n,m = map(int,f.readline().split())
    al,comp = [[] for _ in range(n)],[[] for _ in range(n)]
    st,vis = [],[0]*n
    for _ in range(m):
        u,v = map(int,f.readline().split());u-=1;v-=1
        al[u].append(v); comp[v].append(u)
    def dfs(u):
        vis[u] = 1
        for v in al[u]:
            if not vis[v]:
                dfs(v)
        st.append(u)
    def kosaraju(u):
        vis[u] = 1
        for v in comp[u]:
            if not vis[v]:
                kosaraju(v)
    for u in range(n):
        if not vis[u]: dfs(u)
    vis,scc = [0]*n,0
    while st:
        u = st.pop()
        if not vis[u]:
            scc += 1
            kosaraju(u)
    print(scc)