from collections import deque 
with open('./testcase/rosalind_bfs.txt','r') as f:
    n,m = map(int,f.readline().split())
    al,dist = [[] for _ in range(n)], [-1]*n
    for line in f.readlines():
        u,v = map(int,line.split());u-=1;v-=1;
        al[u].append(v)
q = deque(); 
q.append(0); dist[0] = 0
while q:
    u = q.popleft()
    for v in al[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
print(*dist)
