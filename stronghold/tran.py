dna=[]
with open('./testcase/rosalind_tran.txt','r') as f:
    while line:=f.readline().strip():
        if line[0] == '>': dna.append('')
        else: dna[-1]+= line
ti,tv=0,0
for i,c in enumerate(dna[0]):
    if dna[0][i] == dna[1][i]: continue
    if dna[0][i] in 'AG' and dna[1][i] in 'AG': ti += 1
    elif dna[0][i] in 'CT' and dna[1][i] in 'CT': ti += 1
    else: tv += 1
print(ti/tv)
    
