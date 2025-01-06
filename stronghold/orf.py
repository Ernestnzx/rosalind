import re
from Bio import SeqIO
ans = set()
def orf(s):
    start_idx = [match.start() for match in re.compile('AUG').finditer(str(s))]
    for i in start_idx:
        for j in range(i+3,len(s)-2,3):
            if s[j:j+3] in {'UAG','UGA','UAA'}:
                ans.add(s[i:j].translate())
                break

record = next(SeqIO.parse('./testcase/rosalind_orf.txt','fasta'))
orf(record.seq.transcribe())
orf(record.seq.reverse_complement().transcribe())
for prot in ans: print(prot)