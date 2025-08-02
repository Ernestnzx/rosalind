from collections import *
with open('./testcase/rosalind_ba9k.txt','r') as f:
    t,i = f.readline().strip(),int(f.readline())
    def get_rank(s):
        ranks,counts = [],Counter()
        for i,c in enumerate(s):
            counts[c] += 1
            ranks.append((i,c,counts[c]))
        return ranks
    x,y = get_rank(t),get_rank(sorted(t))
    x,y = {i:(c,r) for i,c,r in x}, {(c,r):i for i,c,r in y}
    print(y[x[i]])