from Bio import SeqIO
s = SeqIO.read('./testcase/rosalind_revp.txt','fasta').seq
n = len(s)
for i in range(n):
    for j in range(4,13):
        t = s[i:i+j]
        if i+j <= n and t == t.reverse_complement():
            print(i+1,j)