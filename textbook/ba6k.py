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

def dfs(u,vis,al,cycle):
    vis.add(u); cycle[-1].append(u)
    for v in al[u]:
        if v not in vis:
            dfs(v,vis,al,cycle)

def graph_to_genome(g):
    al,p,vis,cycles = {},set(),set(),[]
    for u,v in g:
        al.setdefault(u,[]).append(v)
        al.setdefault(v,[]).append(v+1 if v&1 else v-1)
    for i in range(len(al)):
        if i+1 in vis: continue
        cycles.append([])
        dfs(i+1,vis,al,cycles)
    return [tuple(cycle_to_chromosome(cycle)) for cycle in cycles]

def two_break_on_genome_graph(genome_graph:set,i1,i2,j1,j2):
    break_graph = genome_graph.copy()
    if (i1,i2) in break_graph: break_graph.remove((i1,i2)); break_graph.add((i1,j1))
    if (i2,i1) in break_graph: break_graph.remove((i2,i1)); break_graph.add((j1,i1))
    if (j1,j2) in break_graph: break_graph.remove((j1,j2)); break_graph.add((i2,j2))
    if (j2,j1) in break_graph: break_graph.remove((j2,j1)); break_graph.add((j2,i2))
    return break_graph

def two_break_on_genome(p,i1,i2,j1,j2):
    edges = colored_edges(p)
    graph = two_break_on_genome_graph(edges,i1,i2,j1,j2)
    g = graph_to_genome(sorted(graph))
    return g

with open('./testcase/rosalind_ba6k.txt','r') as f:
    p = (eval(f.readline().replace(' ',',')),)
    i1,i2,j1,j2 = eval(f.readline())
    print(' '.join(f"({' '.join(map(lambda x : ('+' if x > 0 else '') + str(x),c))})" for c in two_break_on_genome(p,i1,i2,j1,j2)))
