from ds import sa_lcp
with open('./testcase/rosalind_ba9h.txt','r') as f:
    s = f.readline().strip()
    q = [i.strip() for i in f.readlines()]
    sa,ans = sa_lcp.suffix_array_construction(s+'$'),set()
    for t in q:
        l,r = sa_lcp.string_matching(s,t,sa)
        if l == -1 and r == -1: continue
        ans.update(sa[l:r+1])
    print(*sorted(ans))