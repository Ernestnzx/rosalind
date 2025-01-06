from collections import deque
with open('./testcase/rosalind_dag.txt','r') as f:
    tc = int(f.readline())
    for _ in range(tc):
        f.readline()
        n,m = map(int,f.readline().split())
        al,in_deg = [[] for _ in range(n)],[0]*n
        for _ in range(m):
            u,v = map(int,f.readline().split());u-=1;v-=1
            al[u].append(v); in_deg[v]+=1
        q,topo = deque(),0
        for u in range(n):
            if not in_deg[u]:
                q.append(u)
        while q:
            u = q.popleft()
            topo += 1
            for v in al[u]:
                in_deg[v]-=1
                if in_deg[v]: continue
                q.append(v)
        print(1 if topo == n else -1,end=' ')
