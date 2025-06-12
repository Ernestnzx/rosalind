def neighbors(pattern,d,a='ACGT'):
    if d == 0: return set(pattern)
    if len(pattern) == 1: return a
    neighborhood = set()
    for t in neighbors(pattern[1:],d):
        if sum(a!=b for a,b in zip(pattern[1:],t)) < d:
            for x in a: neighborhood.add(x+t)
        else:
            neighborhood.add(pattern[0]+t)
    return neighborhood

with open('./testcase/rosalind_ba1i.txt','r') as f:
    s = f.readline().strip()
    k,d = map(int,f.readline().split())
    n,c = len(s),{}
    for i in range(n-k+1):
        for t in neighbors(s[i:i+k],d):
            if t not in c: c[t] = 0
            c[t] += 1
    m = max(c.values())
    print(*map(lambda x : x[0], filter(lambda x : x[1] == m, c.items())))