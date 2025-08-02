from ds import sa_lcp
with open('./testcase/rosalind_ba9q.txt','r') as f:
    s,k = f.readline().strip(),int(f.readline())
    print('\n'.join(f'{i},{j}' for i,j in enumerate(sa_lcp.suffix_array_construction(s)) if j%k==0))