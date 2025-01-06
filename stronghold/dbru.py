from Bio.Seq import Seq
s,k = set(),0
with open('./testcase/rosalind_dbru.txt','r') as f:
    for line in f.readlines():
        seq = Seq(line.strip())
        s.add(str(seq))
        s.add(str(seq.reverse_complement()))
        k = len(seq)
for r in sorted(s):
    print(f'({r[:k-1]}, {r[1:k]})')
