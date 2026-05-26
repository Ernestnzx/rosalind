from itertools import *

def g(u):
    if len(u) == 1: return u
    f,*r = u
    ans = []
    for i in range(len(r)):
        for c in combinations(r,i):
            i,j = g([f]+list(c)),g([i for i in r if i not in set(c)])
            for ls in g([f]+list(c)):
                for rs in g([i for i in r if i not in set(c)]):
                    ans.append(f'({ls},{rs})')
    return ans

with open('./testcase/temp.txt','r') as f:
    a = list(f.readline().split())
    print('\n'.join(f'({a[0]},{i});' for i in g(a[1:])))
