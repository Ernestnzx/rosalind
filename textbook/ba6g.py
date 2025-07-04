def cycle_to_chromosome(nodes):
    chromosome = []
    for i in range(len(nodes)//2):
        if nodes[2*i] < nodes[2*i+1]: chromosome.append(nodes[2*i+1]//2)
        else: chromosome.append((-nodes[(2*i)]//2))
    return chromosome

with open('./testcase/rosalind_ba6g.txt','r') as f:
    c = eval(f.readline().strip().replace(' ',','))
    print(f"({' '.join(map(lambda x : ('+' if x > 0 else '') + str(x), cycle_to_chromosome(c)))})")
