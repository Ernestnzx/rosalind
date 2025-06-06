from ds import sa_lcp
s = open('./testcase/rosalind_ling.txt','r').readline().strip()+'$'
n = len(s)-1 # Account for sentinal character
sa = sa_lcp.suffix_array_construction(s)
lcp = sa_lcp.lcp_construction(s,sa)
sub,m = n*(n+1)//2 - sum(lcp), sum([min(4**i,n-i+1) for i in range(1,n+1)])
print(round(sub/m,5))