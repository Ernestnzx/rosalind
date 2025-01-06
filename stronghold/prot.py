from Bio.Seq import Seq
with open('./testcase/rosalind_prot.txt','r') as f:
    print(Seq(f.readline().strip()).transcribe().translate())