from Bio import SeqIO
def f(i,j):
    s = 1
    for i in range(i,j,1): s *= (i+1)
    return s
s = SeqIO.read('./testcase/rosalind_mmch.txt','fasta').seq
a,u,g,c=s.count('A'),s.count('U'),s.count('G'),s.count('C')
if a < u: a,u=u,a
if g < c: g,c=c,g
print(f(a-u,a)*f(g-c,g))