from Bio import SeqIO
def f(n):
    if n <= 1: return 1
    return n*f(n-1)
s = SeqIO.read('./testcase/rosalind_pmch.txt','fasta').seq
c,a = s.count('C'),s.count('A')
print(f(c)*f(a))
