dna,key = [],''
with open('./testcase/rosalind_pdst.txt','r') as f:
    while line:=f.readline().strip():
        if line[0] == '>': dna.append([line,''])
        else: dna[-1][1] += line
n,m=len(dna),len(dna[0][1])
d=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        diff = sum([dna[i][1][k] != dna[j][1][k] for k in range(m)])
        d[i][j] = d[j][i] = diff/m
for i in range(n):
    for j in range(n):
        print(f'{d[i][j]:.5f}',end=' ')
    print()
