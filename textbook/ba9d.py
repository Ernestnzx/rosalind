from ds import sa_lcp
s = open('./testcase/rosalind_ba9d.txt','r').readline().strip()+'$'
sa = sa_lcp.suffix_array_construction(s)
lcp = sa_lcp.lcp_construction(s,sa)
l,i = sa_lcp.longest_repeated_substring(lcp)
print(s[sa[i]:sa[i]+l])