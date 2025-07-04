def cycle_to_chromosome(nodes):
    chromosome = []
    if abs(nodes[0] - nodes[-1]) == 1: nodes = nodes[-1:] + nodes[:-1]
    for i in range(len(nodes)//2):
        if nodes[2*i] < nodes[2*i+1]: chromosome.append(nodes[2*i+1]//2)
        else: chromosome.append((-nodes[(2*i)]//2))
    return chromosome

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
    for i in range(1,len(al)):
        if i in vis: continue
        cycles.append([])
        dfs(i,vis,al,cycles)
    return [tuple(cycle_to_chromosome(cycle)) for cycle in cycles]

with open('./testcase/rosalind_ba6i.txt','r') as f:
    g = eval(f.readline())
    print(''.join(f"({' '.join(map(lambda x : ('+' if x > 0 else '') + str(x),c))})" for c in graph_to_genome(g)))
