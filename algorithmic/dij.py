import heapq
with open('./testcase/rosalind_dij.txt','r') as f:
    INF=int(1e9);n,m=map(int,f.readline().split())
    al,dist= [[] for _ in range(n)],[INF]*n
    for _ in range(m):
        u,v,w=map(int,f.readline().split());u-=1;v-=1
        al[u].append((v,w))
    pq = []
    pq.append((0,0)); dist[0] = 0
    while pq:
        d,u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v,w in al[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq,(dist[v],v))
    print(*map(lambda x:-1 if x == INF else x,dist))
