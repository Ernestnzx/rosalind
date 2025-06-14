def neighbors(pattern,d,a='ACGT'):
    if d == 0: return set(pattern)
    if len(pattern) == 1: return a
    neighborhood,suffix = set(),pattern[1:]
    for t in neighbors(suffix,d):
        if sum(a!=b for a,b in zip(suffix,t)) < d:
            for x in a: neighborhood.add(x+t)
        else:
            neighborhood.add(pattern[0]+t)
    return neighborhood

with open('./testcase/rosalind_ba2a.txt','r') as f:
    k,d = map(int,f.readline().split())
    dna = [s.strip() for s in f.readlines()]
    n,m,a = len(dna),len(dna[0]),[]
    for i in range(n):
        s = set()
        for j in range(m-k+1):
            for t in neighbors(dna[i][j:j+k],d):
                s.add(t)
        a.append(s)
    print(*set.intersection(*a))
