from math import sqrt

with open('./testcase/rosalind_pdpl.txt','r') as f:
    l = list(sorted([int(i) for i in f.readline().split()]))
    n = int((1+sqrt(1+2*4*len(l)))/2)
    width = l.pop()
    x = [0,width]

    def delta(y,X,L):
        D = [abs(x-y) for x in X]
        for d in D:
            if d not in L:
                return False
        return D

    def backtrack(L,X):
        if not L: 
            return True
        y = max(L)
        l,r = delta(y,X,L), delta(width-y,X,L)
        if l:
            X.append(y)
            for i in l: L.remove(i)
            if backtrack(L,X):
                return True
            X.pop(); L.extend(l)
        if r:
            X.append(width-y)
            for i in r: L.remove(i)
            if backtrack(L,X):
                return True
            X.pop(); L.extend(r)
        return False

    backtrack(l,x)
    assert(n == len(x))
    print(*sorted(x))
