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

with open('./testcase/rosalind_ba3k.txt','r') as f:
    al,in_deg,out_deg = {},Counter(),Counter()
    for s in [s.strip() for s in f.readlines()]:
        u,v = s[:-1],s[1:]
        if u not in al: al[u] = []
        if v not in al: al[v] = []
        al[u].append(v)
        in_deg[v]+=1; out_deg[u]+=1
    contigs = maximal_non_branching_paths(al)
    print(*[s[0] + ''.join(s[i][-1] for i in range(1,len(s))) for s in contigs],sep='\n')
