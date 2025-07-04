def chromosome_to_cycle(c):
    nodes = []
    for i,s in enumerate(c):
        if s > 0: nodes.extend([2*s-1,2*s])
        else: nodes.extend([-2*s,-2*s-1])
    return nodes

with open('./testcase/rosalind_ba6f.txt','r') as f:
    p = eval(f.readline().strip().replace(' ',','))
    print(str(tuple(chromosome_to_cycle(p))).replace(',',''))