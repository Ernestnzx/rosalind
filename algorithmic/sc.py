from collections import deque
with open('./testcase/rosalind_sc.txt','r') as f:
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
                if m[u] == m[v] or m[v] in dag[m[u]]: continue
                in_deg[m[v]]+=1
                dag[m[u]].add(m[v])
        q,vis,topo = deque(),[0]*scc,[]
        for u in range(scc):
            if not in_deg[u]:
                q.append(u)
        while q:
            u = q.popleft()
            topo.append(u)
            for v in dag[u]:
                in_deg[v]-=1
                if not in_deg[v]:
                    q.append(v)
        assert(len(topo) == scc)
        ans = 1
        for i in range(scc-1):
            if topo[i+1] not in dag[i]:
                ans = -1
                break
        print(ans,end=' ')