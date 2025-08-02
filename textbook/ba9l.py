from collections import *
def get_lf_array(s):
    def get_rank(s):
        ranks,counts = [],Counter()
        for i,c in enumerate(s):
            counts[c] += 1
            ranks.append((i,c,counts[c]))
        return ranks
    x,y = get_rank(s),get_rank(sorted(s))
    x,y = {i:(c,r) for i,c,r in x}, {(c,r):i for i,c,r in y}
    return [y[x[i]]for i in x]

def BWMatching(last_column,pattern,last_to_first):
    n = len(last_column)
    top,bottom = 0,n-1
    while top <= bottom:
        if pattern:
            symbol,pattern = pattern[-1],pattern[:-1]
            matches = [i for i in range(top,bottom+1) if last_column[i] == symbol]
            if not matches: return 0
            top,bottom = last_to_first[matches[0]],last_to_first[matches[-1]]
        else:
            return bottom-top+1

with open('./testcase/rosalind_ba9l.txt','r') as f:
    s = f.readline().strip()
    q = [i.strip() for i in f.readline().split()]
    lf_arr = get_lf_array(s)
    print(' '.join(str(BWMatching(s,p,lf_arr)) for p in q))