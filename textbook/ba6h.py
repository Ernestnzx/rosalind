def chromosome_to_cycle(c):
    nodes = []
    for i,s in enumerate(c):
        if s > 0: nodes.extend([2*s-1,2*s])
        else: nodes.extend([-2*s,-2*s-1])
    return nodes

def colored_edges(genome):
    edges = set()
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome);
        nodes.append(nodes[0])
        for i in range(len(chromosome)):
            edges.add((nodes[2*i+1],nodes[2*i+2]))
    return edges

with open('./testcase/rosalind_ba6h.txt','r') as f:
    c = eval(f.readline().strip().replace(' ',',').replace(')(','),('))
    print(', '.join(map(lambda x : str(x),sorted(colored_edges(c)))))
