import heapq
with open('./testcase/rosalind_cte.txt','r') as f:
    INF=int(1e9)
    tc=int(f.readline())
    for _ in range(tc):
        # f.readline()
        n,m=map(int,f.readline().split())
        al = [[] for _ in range(n)]
        s,t,w1 = map(int,f.readline().split());s-=1;t-=1
        for _ in range(m-1):
            u,v,w=map(int,f.readline().split());u-=1;v-=1
            al[u].append((v,w))
        pq,dist = [(0,t)],[INF]*n
        dist[t] = 0
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]: continue
            for v,w in al[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w;
                    heapq.heappush(pq,(dist[v],v))
        print(dist[s]+w1 if dist[s] != INF else -1,end=' ')