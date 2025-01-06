from Bio import Phylo
from io import StringIO
with open('./testcase/rosalind_nkew.txt','r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
for i in range(0,len(lines),2):
    u,v = lines[i+1].split()
    print(int(Phylo.read(StringIO(lines[i]),'newick').distance(u,v)),end=' ')
