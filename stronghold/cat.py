from Bio import SeqIO
s = SeqIO.read('./testcase/rosalind_cat.txt','fasta').seq
c,a,mod=s.count('C'),s.count('A'),1000000
cat = [0 for _ in range(151)]
cat[0] = 1 
for i in range(1,151):
    cat[i] = int((4*i-2)/(i+1)*cat[i-1])%mod
print((cat[c]*cat[a])%mod)
