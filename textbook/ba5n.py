from collections import *

def dfs(u):
    global topo,al,vis
    vis.add(u)
    for v in al[u]:
        if v not in vis:
            dfs(v)
    topo.append(u)

with open('./testcase/rosalind_ba5n.txt','r') as f:
    al,in_deg = {},Counter()
    for s in f.readlines():
        u,neigh = s.split('->')
        u,neigh = int(u),list(map(int,neigh.split(',')))
        for v in neigh:
            al.setdefault(u,[]).append(v)
            al.setdefault(v,[])
            in_deg[u] = in_deg[u]
            in_deg[v] += 1
    vis,topo = set(),[]
    for u,c in in_deg.items():
        if c or u in vis: continue
        dfs(u)
    print(', '.join(map(str,topo[::-1])))
