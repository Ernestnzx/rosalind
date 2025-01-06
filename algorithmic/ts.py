from collections import deque
with open('./testcase/rosalind_ts.txt','r') as f:
    n,m = map(int,f.readline().split())
    al,in_deg = [[] for _ in range(n)],[0]*n
    for _ in range(m):
        u,v = map(int,f.readline().split());u-=1;v-=1
        al[u].append(v); in_deg[v]+=1
    q,topo = deque(),[]
    for u in range(n):
        if not in_deg[u]:
            q.append(u)
    while q:
        u = q.popleft()
        topo.append(u+1)
        for v in al[u]:
            in_deg[v]-=1
            if in_deg[v]: continue
            q.append(v)
    print(*topo)
