from ds import sa_lcp
def get_occ(s):
    s,n = sorted(s),len(s)
    return {s[0]:0} | {s[i]:i for i in range(1,n) if s[i-1] != s[i]}

def get_count(s,occ):
    n = len(s)
    count = [{i:0 for i in occ} for _ in range(n+1)]
    for i,c in enumerate(s):
        count[i+1][c] += 1
        for d in occ: count[i+1][d] += count[i][d]
    return count

def betterBWMatching(occ,last_column,pattern,count):
    top,bottom = 0,len(last_column)-1
    while top <= bottom:
        if pattern:
            symbol,pattern = pattern[-1],pattern[:-1]
            if symbol not in occ: return 0
            top = occ[symbol] + count[top][symbol]
            bottom = occ[symbol] + count[bottom+1][symbol] - 1
        else:
            return bottom-top+1
    return 0

with open('./testcase/rosalind_ba9n.txt','r') as f:
    s = f.readline().strip(); s += '$'
    q = [i.strip() for i in f.readlines()]
    sa,n = sa_lcp.suffix_array_construction(s),len(s)
    bws =''.join(s[sa[i]-1] if sa[i] else '$' for i in range(n)) 
    occ = get_occ(bws); count = get_count(bws,occ)
    ans = set()
    for t in q:
        l,r = sa_lcp.string_matching(s,t,sa)
        if l == -1 and r == -1: continue
        ans.update(sa[l:r+1])
    print(*sorted(ans))
