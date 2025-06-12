from math import comb
with open('./testcase/rosalind_cntq.txt','r') as f:
    n = int(f.readline())
    s = f.readline().strip()
    print(comb(n,4)%int(1e6))
