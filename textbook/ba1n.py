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

with open('./testcase/rosalind_ba1n.txt','r') as f:
    s,d = f.readline().strip(),int(f.readline())
    for i in sorted(neighbors(s,d)): print(i)