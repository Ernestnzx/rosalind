dna,key = [],''
with open('./testcase/rosalind_grph.txt','r') as f:
    while line:=f.readline().strip():
        if line[0] == '>': dna.append([line,''])
        else: dna[-1][1] += line
n,e = len(dna),[]
for i in range(n):
    for j in range(n):
        if i == j: continue
        if dna[i][1][-3:] == dna[j][1][:3]:
            e.append((dna[i][0],dna[j][0]))
for u,v in e:
    print(f'{u[1:]} {v[1:]}')
