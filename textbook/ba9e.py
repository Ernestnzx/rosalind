from ds import sa_lcp
with open('./testcase/rosalind_ba9e.txt','r') as f:
    s,t = f.readline().strip(),f.readline().strip()
    u = s+'#'+t+'$';
    sa = sa_lcp.suffix_array_construction(u)
    lcp = sa_lcp.lcp_construction(u,sa)
    l,i = sa_lcp.longest_common_substring(sa,lcp,len(s))
    print(u[sa[i]:sa[i]+l])