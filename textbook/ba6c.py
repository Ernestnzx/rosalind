import sys; sys.setrecursionlimit(10**5)

def chromosome_to_cycle(c):
    nodes = []
    for i,s in enumerate(c):
        if s > 0: nodes.extend([2*s-1,2*s])
        else: nodes.extend([-2*s,-2*s-1])
    return nodes

def colored_edges(genome):
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome);
        nodes.append(nodes[0])
        for i in range(len(chromosome)):
            edges.append((nodes[2*i+1],nodes[2*i+2]))
    return edges

def cycles(p,q):
    al,cycles,vis = {},0,set()
    for u,v in colored_edges(p)+colored_edges(q):
        al.setdefault(u,[]).append(v)
        al.setdefault(v,[]).append(u)
    def dfs(u):
        vis.add(u)
        for v in al[u]:
            if v not in vis:
                dfs(v)
    for u in range(len(al)):
        if u+1 in vis: continue
        dfs(u+1); cycles+=1
    return cycles

with open('./testcase/rosalind_ba6c.txt','r') as f:
    p = eval(f'({f.readline().replace(' ',',').replace(')(','),(')},)')
    q = eval(f'({f.readline().replace(' ',',').replace(')(','),(')},)')
    print(sum(len(i) for i in p) - cycles(p,q))
