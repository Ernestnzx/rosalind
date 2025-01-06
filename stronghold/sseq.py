from Bio import SeqIO
s,t = SeqIO.parse('./testcase/rosalind_sseq.txt','fasta')
idx = 0
for i in range(len(s)):
    if idx < len(t) and s[i] == t[idx]:
        print(i+1)
        idx += 1
