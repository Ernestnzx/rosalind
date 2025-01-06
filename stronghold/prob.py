import numpy as np
with open('./testcase/rosalind_prob.txt','r') as f:
    dna = f.readline().strip()
    probs = list(map(float,f.readline().split()))
for prob in probs:
    ans = 0
    for c in dna:
        ans += np.log10(prob/2) if c == 'G' or c == 'C' else np.log10((1-prob)/2)
    print(f'{ans:.3f}',end=' ')