import sys
dna,key = {},''
with open('./testcase/rosalind_lcsm.txt','r') as f:
    while line:=f.readline().strip():
        if line[0] == '>': dna[key:=line] = ''
        else: dna[key] += line
s,mv='',1e9
for k,v in dna.items():
    if mv > len(v):
        mv,s = len(v),v
n=len(s)
substrs=set([s[i:j+1] for i in range(n) for j in range(i,n)])
for substr in sorted(substrs,key=lambda x : -len(x)):
    is_found=True
    for k,v in dna.items():
        if substr not in v: is_found=False; break
    if is_found: print(substr); sys.exit(0)
