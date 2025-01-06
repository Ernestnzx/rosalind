from Bio import Phylo
from io import StringIO
with open('./testcase/rosalind_nwck.txt','r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
n = len(lines)
for i in range(0,n,2):
    tree = Phylo.read(StringIO(lines[i]),'newick')
    for clade in tree.find_clades():
        if clade.branch_length is None:
            clade.branch_length = 1
    u,v = lines[i+1].split()
    print(tree.distance(u,v),end=' ')
