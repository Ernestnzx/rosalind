from itertools import product
from Bio import SeqIO
s,d=SeqIO.read('./testcase/rosalind_kmer.txt','fasta').seq,{}
for kmer in product('ACGT',repeat=4): d[''.join(kmer)] = 0
for substr in [s[i:i+4] for i in range(len(s)-3)]: d[substr] += 1
for k,v in d.items(): print(v,end=' ')
