with open('./testcase/rosalind_bf.txt','r') as f:
    INF=int(1e9)
    n,m=map(int,f.readline().split())
    el,dist=[],[INF]*n
    for line in f.readlines():
        u,v,w=map(int,line.split())
        el.append((u-1,v-1,w))
    dist[0]=0
    for _ in range(n-1):
        for u,v,w in el:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    print(*map(lambda x : 'x' if x == INF else x,dist))
