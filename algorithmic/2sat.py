from sys import setrecursionlimit
setrecursionlimit(10**5)
with open('./testcase/temp.txt','r') as f:
    tc = int(f.readline())
    for _ in range(tc):
        f.readline()
        n,m = map(int,f.readline().split())
        al,comp = {},{}
        for i in range(1,n+1):
            al[i],al[-i] = set(),set()
            comp[i],comp[-i] = set(),set()
        for _ in range(m):
            a,b = map(int,f.readline().split())
            al[-a].add(b); al[-b].add(a)
            comp[a].add(-b); comp[b].add(-a)
        st,vis=[],set()
        def dfs(u):
            vis.add(u)
            for v in al[u]:
                if v not in vis:
                    dfs(v)
            st.append(u)
        def kosaraju(u,scc):
            vis.add(u)
            m[u] = scc
            for v in comp[u]:
                if v not in vis:
                    kosaraju(v,scc)
        for u in al:
            if u not in vis:
                dfs(u)
        vis.clear()
        scc,m= 0,{}
        while st:
            u = st.pop()
            if u not in vis:
                kosaraju(u,scc)
                scc += 1
        ans = 1
        assign = [0]*(n+1)
        for u in range(1,n+1):
            if m[u] == m[-u]: ans = 0; break
            assign[u] = m[u] > m[-u]
        print(ans,end=' ')
        if ans:
            for i,v in enumerate(assign[1:]):
                print(i+1 if v else -(i+1),end=' ')
        print()