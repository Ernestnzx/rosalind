from ds import sa_lcp
with open('./testcase/rosalind_ba9g.txt','r') as f:
    print(', '.join(str(i) for i in sa_lcp.suffix_array_construction(f.readline().strip())))