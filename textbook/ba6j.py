def two_break_on_genome_graph(genome_graph:set,i1,i2,j1,j2):
    break_graph = genome_graph.copy()
    if (i1,i2) in break_graph: break_graph.remove((i1,i2)); break_graph.add((i1,j1))
    if (i2,i1) in break_graph: break_graph.remove((i2,i1)); break_graph.add((j1,i1))
    if (j1,j2) in break_graph: break_graph.remove((j1,j2)); break_graph.add((i2,j2))
    if (j2,j1) in break_graph: break_graph.remove((j2,j1)); break_graph.add((j2,i2))
    return break_graph

with open('./testcase/rosalind_ba6j.txt','r') as f:
    e = set(eval(f.readline()))
    i1,i2,j1,j2 = eval(f.readline())
    print(', '.join(map(lambda x : str(x), sorted(two_break_on_genome_graph(e,i1,i2,j1,j2)))))
