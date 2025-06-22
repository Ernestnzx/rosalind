def dfs(u,vis,al,topo):
    vis.add(u)
    for v,w in al[u]:
        if v not in vis:
            dfs(v,vis,al,topo)
    topo.append(u)

with open('./testcase/rosalind_ba5d.txt','r') as f:
    s = int(f.readline()); t = int(f.readline())
    al = {}
    for temp in f.readlines():
        u,vw = temp.strip().split('->')
        v,w = vw.split(':')
        al.setdefault(int(v),[])
        al.setdefault(int(u),[]).append((int(v),int(w)))
    topo = []; dfs(s,set(),al,topo)
    dist,parent = [0]*(max(al)+1),[i for i in range(max(al)+1)]
    for u in topo[::-1]:
        for v,w in al[u]:
            if dist[v] <= dist[u] + w:
                dist[v],parent[v] = dist[u]+w,u
    path = []
    print(dist[t])
    while parent[t] != t:
        path.append(t)
        t = parent[t]
    path.append(t)
    print('->'.join(map(str,path[::-1])))
