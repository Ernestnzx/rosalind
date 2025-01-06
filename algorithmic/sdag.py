from collections import deque
with open('./testcase/rosalind_sdag.txt','r') as f:
    INF=int(1e9)
    n,m=map(int,f.readline().split())
    al,dist,in_deg = [[] for _ in range(n)],[INF]*n,[0]*n
    for line in f.readlines():
        u,v,w=map(int,line.split())
        al[u-1].append((v-1,w)); in_deg[v-1]+=1
    q,topo = deque(),[]
    for u in range(n):
        if not in_deg[u]:
            q.append(u)
    while q:
        u = q.popleft() 
        topo.append(u)
        for v,w in al[u]:
            in_deg[v]-=1
            if not in_deg[v]:
                q.append(v)
    dist[0] = 0
    for u in topo:
        for v,w in al[u]:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    print(*map(lambda x : 'x' if x == INF else x, dist))