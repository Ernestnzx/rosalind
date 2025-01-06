from Bio.Seq import Seq
dna,s={},''
with open('./testcase/rosalind_splc.txt','r') as f:
    while line:=f.readline().strip():
        if not s: s=line
        if line[0] == '>': dna[key:=line] = ''
        else: dna[key]+= line
for k,v in dna.items():
    if k == s: continue
    dna[s] = dna[s].replace(v,'')
print(Seq(dna[s]).transcribe().translate())
