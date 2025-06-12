from Bio.Seq import Seq
print(Seq(open('./testcase/rosalind_ba1c.txt').readline().strip()).reverse_complement())