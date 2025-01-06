from Bio.Seq import Seq
print(Seq(open('./testcase/rosalind_revc.txt','r').readline().strip()).reverse_complement())