from copy import *

def chromosome_to_cycle(c):
    nodes = []
    for i,s in enumerate(c):
        if s > 0: nodes.extend([2*s-1,2*s])
        else: nodes.extend([-2*s,-2*s-1])
    return nodes

def cycle_to_chromosome(nodes):
    chromosome = []
    if abs(nodes[0] - nodes[-1]) == 1: nodes = nodes[-1:] + nodes[:-1]
    for i in range(len(nodes)//2):
        if nodes[2*i] < nodes[2*i+1]: chromosome.append(nodes[2*i+1]//2)
        else: chromosome.append((-nodes[(2*i)]//2))
    return chromosome

def colored_edges(genome):
    edges = set()
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome);
        nodes.append(nodes[0])
        for i in range(len(chromosome)):
            edges.add((nodes[2*i+1],nodes[2*i+2]))
    return edges

def graph_to_genome(g):
    al,vis,cycles = {},set(),[]
    for u,v in g:
        al.setdefault(u,[]).append(v)
        al.setdefault(v,[]).append(v+1 if v&1 else v-1)
    def dfs(u,vis,al,cycle):
        vis.add(u); cycle[-1].append(u)
        for v in al.get(u,[]):
            if v not in vis:
                dfs(v,vis,al,cycle)
    for u in al:
        if u in vis: continue
        cycles.append([])
        dfs(u,vis,al,cycles)
    return [tuple(cycle_to_chromosome(cycle)) for cycle in cycles]

def two_break_on_genome_graph(genome_graph,i1,i2,j1,j2):
    break_graph = deepcopy(genome_graph)
    if (i1,i2) in break_graph: break_graph.remove((i1,i2)); break_graph.add((i1,j1))
    if (i2,i1) in break_graph: break_graph.remove((i2,i1)); break_graph.add((j1,i1))
    if (j1,j2) in break_graph: break_graph.remove((j1,j2)); break_graph.add((i2,j2))
    if (j2,j1) in break_graph: break_graph.remove((j2,j1)); break_graph.add((j2,i2))
    return break_graph

def two_break_on_genome(p,i1,i2,j1,j2):
    edges = colored_edges(p)
    graph = two_break_on_genome_graph(edges,i1,i2,j1,j2)
    return graph_to_genome(graph)

def non_trivial_cycle(al,blue_edges):
    vis,cycles = set(),[]
    def dfs(u):
        vis.add(u);
        for v in al[u]:
            if v not in vis:
                if (u,v) in blue_edges: cycles.append((u,v))
                if (v,u) in blue_edges: cycles.append((v,u))
                dfs(v)
    for u in al:
        if u in vis: continue
        dfs(u);
    return cycles

# Can't figure out what's wrong here, will get back to it.
def shortest_rearrangement(p,q):
    al = {}
    red_edges,blue_edges = colored_edges(p), colored_edges(q)
    for u,v in red_edges | blue_edges:
        al.setdefault(u,set()).add(v)
        al.setdefault(v,set()).add(u)
    while edge := non_trivial_cycle(al,blue_edges):
        j1,i2 = edge.pop()
        i1 = next((a if j1 == b else b) for a,b in red_edges if a == j1 or b == j1)
        j2 = next((b if i2 == a else a) for a,b in red_edges if a == i2 or b == i2)
        if (j1,i1) in red_edges: i1,j1 = j1,i1
        if (i2,j2) in red_edges: j2,i2 = i2,j2
        p = two_break_on_genome(p,i1,j1,i2,j2)
        for u,v in colored_edges(p) | blue_edges:
            al.setdefault(u,set()).add(v)
            al.setdefault(v,set()).add(u)
        print(p)

with open('./testcase/temp.txt','r') as f:
    p = eval(f'({f.readline().replace(' ',',').replace(')(','),(')},)')
    q = eval(f'({f.readline().replace(' ',',').replace(')(','),(')},)')
    shortest_rearrangement(p,q)
    # print(''.join(f"({' '.join(f'{('+' if v > 0 else '')}{v}' for v in t)})" for t in l))
