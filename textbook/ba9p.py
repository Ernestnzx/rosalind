from collections import *
with open('./testcase/rosalind_ba9p.txt','r') as f:
    t,in_order = {},Counter()
    while True:
        s = f.readline().strip()
        if s == '-': break
        u,neigh = s.split('->')
        u,neigh = int(u),tuple(eval(neigh.replace('{}','()').strip()))
        t[u] = neigh
        for v in neigh: in_order[v] += 1
    color = {}
    for s in f.readlines():
        u,c = s.strip().split(': ')
        color [int(u)] = c.strip()
    for i in t: color.setdefault(i,'grey')
    topo,vis,root = [],set(),[i for i in t if i not in in_order]
    def dfs(u):
        vis.add(u)
        for v in t[u]:
            if v not in vis:
                dfs(v)
        topo.append(u)
    assert(len(root) == 1)
    dfs(root[0])
    for u in topo:
        if color[u] != 'grey': continue
        is_red,is_blue = 0,0
        for v in t[u]:
            if color.get(v) == 'red': is_red = 1
            elif color.get(v) == 'blue': is_blue = 1
            else: is_red,is_blue = 1,1
        if is_red and is_blue:
            color[u] = 'purple'
        elif is_red:
            color[u] = 'red'
        elif is_blue:
            color[u] = 'blue'
    print('\n'.join(f'{k}: {v}' for k,v in sorted(color.items())))
