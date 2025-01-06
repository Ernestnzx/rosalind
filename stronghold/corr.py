from Bio import SeqIO
dna,org={},set()
for r in SeqIO.parse('./testcase/rosalind_corr.txt','fasta'):
    seq,seq_rc = r.seq,r.seq.reverse_complement()
    org.add(seq)
    dna[seq] = 1 if seq not in dna else dna[seq]+1
    dna[seq_rc] = 1 if seq_rc not in dna else dna[seq_rc]+1
a = [k for k,v in dna.items() if v > 1]
b = [k for k,v in dna.items() if v == 1 and k in org]
for i in b:
    for j in a:
        jc = j.reverse_complement()
        c = len([x for x,y in zip(i,j) if x != y])
        rc = len([x for x,y in zip(i,jc) if x != y])
        if c == 1: print(f'{i}->{j}'); break
        if rc == 1: print(f'{i}->{jc}'); break
