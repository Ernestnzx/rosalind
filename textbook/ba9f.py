from ds import sa_lcp
with open('./testcase/rosalind_ba9f.txt','r') as f:
    s,t = f.readline().strip(),f.readline().strip()
    sa = sa_lcp.suffix_array_construction(t+'$')
    n = len(s)
    # O(n^2) solution, Suffix Tree would be more efficient here.
    for i in range(n):
        for j in range(i+1,n+1):
            l,idx = sa_lcp.string_matching(t,s[i:j],sa)
            if l != -1: continue
            print(s[i:j])
            exit(0)
