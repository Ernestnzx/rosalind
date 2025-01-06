from ds.sa_lcp import suffix_array_construction, lcp_construction, string_matching

with open('./testcase/rosalind_subs.txt','r') as f:
    s,t=f.readline().strip(),f.readline().strip()
sa = suffix_array_construction(s)
lcp = lcp_construction(s,sa)
lo,hi=string_matching(s,t,sa)
for i in sorted(sa[lo:hi+1]): print(i+1,end=' ')
