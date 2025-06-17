with open('./testcase/rosalind_ba4m.txt','r') as f:
    l = list(filter(lambda x:x>0,map(int,f.readline().split())))
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
    print(*sorted(x))