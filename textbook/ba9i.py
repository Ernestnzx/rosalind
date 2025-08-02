from ds import sa_lcp
with open('./testcase/rosalind_ba9i.txt','r') as f:
    s = f.readline().strip(); n = len(s)
    sa = sa_lcp.suffix_array_construction(s)
    print(''.join(s[sa[i]-1] if sa[i] else '$' for i in range(n)))
