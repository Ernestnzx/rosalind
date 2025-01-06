from Bio import SeqIO,Align
from Bio.Align import substitution_matrices
print(int(Align.PairwiseAligner(substitution_matrix=substitution_matrices.load('BLOSUM62'),gap_score=-5.0).align(*map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_glob.txt','fasta'))).score))
