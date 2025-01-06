from collections import deque
with open('./testcase/rosalind_gs.txt','r') as f:
    tc = int(f.readline())
    for _ in range(tc):
        f.readline()
        n,m = map(int,f.readline().split())
        al,comp= [[] for _ in range(n)],[[] for _ in range(n)]
        for _ in range(m):
            u,v = map(int,f.readline().split());u-=1;v-=1
            al[u].append(v); comp[v].append(u)
        st,vis,m=[],[0]*n,{}

        def dfs(u):
            vis[u] = 1
            for v in al[u]:
                if not vis[v]:
                    dfs(v)
            st.append(u)

        def kosaraju(u,scc):
            vis[u],m[u] = 1,scc
            for v in comp[u]:
                if not vis[v]:
                    kosaraju(v,scc)

        for u in range(n):
            if not vis[u]: dfs(u)
        vis,scc = [0]*n,0
        while st:
            u = st.pop()
            if not vis[u]:
                kosaraju(u,scc)
                scc+=1
        dag,in_deg = [set() for _ in range(scc)],[0]*scc
        for u in range(n):
            for v in al[u]:
                if m[u] == m[v]: continue
                dag[m[u]].add(m[v])
                in_deg[m[v]]+=1
        count = {}
        for v in in_deg:
            if v not in count: count[v] = 1
            else: count[v] += 1
        if count[0] > 1:
            print(-1,end=' ')
        else:
            for k,v in m.items():
                if v == 0:
                    print(k+1,end=' ')
                    break