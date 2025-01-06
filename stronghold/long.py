from Bio import SeqIO

prot = []
for record in SeqIO.parse('./testcase/rosalind_long.txt','fasta'):
    prot.append(record.seq)
n = len(prot)
al,in_order = [None for _ in range(n)],[0]*n
for i in range(n):
    for j in range(n):
        if i == j: continue
        p1,p2 = prot[i],prot[j]
        s1,s2 = len(p1),len(p2)
        for k in range(min(s1,s2),min(s1,s2)//2,-1):
            if p2[:k] == p1[s1-k:]:
                al[i] = (j,k)
                in_order[j] += 1
                break
u = in_order.index(0); s = prot[u]
while al[u]:
    v,k = al[u]; p = prot[v]
    s += p[k:]
    u = v
print(s)