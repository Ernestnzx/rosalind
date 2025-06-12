from Bio.Seq import Seq
from collections import Counter

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

def count(s,k,d):
    n,c = len(s),Counter()
    for i in range(n-k+1):
        for t in neighbors(s[i:i+k],d):
            c[t] += 1
    return c

with open('./testcase/rosalind_ba1j.txt','r') as f:
    s = Seq(f.readline().strip())
    k,d = map(int,f.readline().split())
    c = count(s,k,d) + count(s.reverse_complement(),k,d)
    m = max(c.values())
    print(*map(lambda x : x[0], filter(lambda x : x[1] == m, c.items())))
