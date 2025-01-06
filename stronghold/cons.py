m,d,dna,key=[],{'A':0,'C':1,'G':2,'T':3},{},''
with open('./testcase/rosalind_cons.txt','r') as f:
    while line:=f.readline().strip():
        if line[0] == '>': dna[key:=line] = ''
        else: dna[key]+= line
consensus,n = '',len(dna[key])
p=[[0 for _ in range(n)] for _ in range(4)]
for k,v in dna.items():
    for i,b in enumerate(v):
        p[d[b]][i] += 1
for i in range(n):
    idx,mv=0,0
    for j in range(4):
        if mv < p[j][i]:
            mv,idx=p[j][i],j
    consensus += 'ACGT'[idx]
print(consensus)
for i in range(4):
    print(f'{"ACGT"[i]}: ',end='')
    for j in range(n):
        print(p[i][j],end=' ')
    print()
