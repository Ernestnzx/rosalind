s,d = open('./testcase/rosalind_dna.txt','r').readline(),{}
for c in s:
    if c not in d: d[c] = 1
    else: d[c] += 1
print(d['A'],d['C'],d['G'],d['T'])
