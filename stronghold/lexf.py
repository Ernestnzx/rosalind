from itertools import product
with open('./testcase/rosalind_lexf.txt','r') as f:
    a,n=''.join(f.readline().strip().split()),int(f.readline())
    for kmer in product(a,repeat=n):
        print(''.join(kmer))
