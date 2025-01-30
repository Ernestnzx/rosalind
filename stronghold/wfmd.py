import numpy as np
with open('./testcase/rosalind_wfmd.txt','r') as f:
    n,m,g,k = map(int,f.readline().split()); c = 0
    iter = int(1e7)
    # monte-carlo cause I can't math :")
    for _ in range(iter):
        mc = m;
        for _ in range(g):
            p = mc/(2*n)
            mc = np.random.binomial(2*n,p)
        if 2*n-mc >= k: c += 1
    print(round(c/iter,3))