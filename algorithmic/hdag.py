from collections import deque
with open('./testcase/rosalind_hdag.txt','r') as f:
    INF=int(1e9)
    tc=int(f.readline())
    for _ in range(tc):
        f.readline()
        n,m=map(int,f.readline().split())
        al,dist,in_deg = [[] for _ in range(n)],[0]*n,[0]*n
        for _ in range(m):
            u,v=map(int,f.readline().split());u-=1;v-=1
            al[u].append(v); in_deg[v] += 1
        q,topo = deque(),[]
        for u in range(n):
            if not in_deg[u]: q.append(u)
        while q:
            u = q.popleft()
            topo.append(u)
            for v in al[u]:
                in_deg[v] -= 1
                if not in_deg[v]: q.append(v)
        parent = [i for i in range(n)]
        for u in topo:
            for v in al[u]:
                if dist[v] < dist[u] + 1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
        if n-1 not in dist: print(-1); continue
        idx,ans = dist.index(n-1),[]
        while idx != parent[idx]:
            ans.append(idx+1)
            idx = parent[idx]
        ans.append(idx+1); ans.append(1)
        print(*ans[::-1])