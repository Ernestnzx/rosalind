from collections import deque
with open('./testcase/rosalind_nwc.txt','r') as f:
    INF=int(1e9)
    tc = int(f.readline())
    for _ in range(tc):
        n,m = map(int,f.readline().split())
        el,dist = [],[0]*n
        for _ in range(m):
            u,v,w = map(int,f.readline().split());
            el.append((u-1,v-1,w))
        for _ in range(n-1):
            for u,v,w in el:
                if dist[u] != INF and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        ans,is_relax,vis=0,1,[0]*n
        while is_relax and not ans:
            is_relax = 0
            for u,v,w in el:
                if dist[u] != INF and not vis[v] and dist[v] > dist[u] + w:
                    ans = 1
        print(1 if ans else -1,end=' ') 