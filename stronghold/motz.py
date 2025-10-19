from Bio import SeqIO
from functools import lru_cache
s = SeqIO.read('./testcase/rosalind_motz.txt','fasta').seq
pairs,MOD={('A','U'),('U','A'),('C','G'),('G','C')},10**6
@lru_cache(maxsize=None)
def f(i,j):
    if i >= j: return 1
    total = f(i+1,j)
    for k in range(i+1,j+1,1):
        if (s[i],s[k]) in pairs:
            total += f(i+1,k-1)*f(k+1,j)
    return total % MOD
print(f(0,len(s)-1))