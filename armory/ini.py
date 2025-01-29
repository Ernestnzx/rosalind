from Bio.Seq import Seq
s = Seq(open('./testcase/rosalind_ini.txt','r').readline().strip())
print(f'{s.count('A')} {s.count('C')} {s.count('G')} {s.count('T')}')