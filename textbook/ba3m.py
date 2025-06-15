from collections import *

def maximal_non_branching_paths(al):
    global in_deg,out_deg
    paths,vis = [],set()
    for u,neigh in al.items():
        if not (in_deg[u] == out_deg[u] == 1) and out_deg[u] > 0:
            vis.add(u)
            for v in neigh:
                non_branching_paths = [u,v]
                vis.add(v)
                while in_deg[v] == out_deg[v] == 1:
                    w = al[v][0]; vis.add(w)
                    non_branching_paths.append(w)
                    v = w
                paths.append(non_branching_paths)
    for u,neigh in al.items():
        if u in vis or not (in_deg[u] == out_deg[u] == 1): continue
        cycle = [u]; vis.add(u)
        v = neigh[0]
        while in_deg[v] == out_deg[v] == 1 and v not in vis:
            cycle.append(v)
            vis.add(v)
            v = al[v][0]
        if v == u: 
            cycle.append(u)
            paths.append(cycle)
    return paths

with open('./testcase/rosalind_ba3m.txt','r') as f:
    al,in_deg,out_deg = {},Counter(),Counter()
    for s in f.readlines():
        u,v = s.split('->'); u = int(u)
        al[u] = list(map(int,v.split(',')))
        out_deg[u] += len(al[u])
        for w in al[u]:
            if w not in al: al[w] = []
            in_deg[w]+=1;
    paths = maximal_non_branching_paths(al)
    print(*[' -> '.join(map(str,path)) for path in paths],sep='\n')
