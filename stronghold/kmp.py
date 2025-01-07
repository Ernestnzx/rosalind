from Bio import SeqIO
s = SeqIO.read('./testcase/rosalind_kmp.txt','fasta').seq
a,n = [0]*len(s),len(s)
for i in range(1,n):
    j = a[i-1]
    while j and s[i] != s[j]: j = a[j-1]
    if s[i] == s[j]: j+=1
    a[i] = j
print(*a)