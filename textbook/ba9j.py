from collections import *
with open('./testcase/rosalind_ba9j.txt','r') as f:
    s = f.readline().strip()
    t = sorted(s)
    def get_rank(s):
        ranks,counts = [],Counter()
        for c in s:
            counts[c] += 1
            ranks.append((c,counts[c]))
        return ranks
    r1,r2 = get_rank(t),get_rank(s)
    lf = {l:f for f,l in zip(r1,r2)}
    ans,u = [],('$',1)
    for _ in range(len(s)):
        u = lf[u]
        ans.append(u[0])
    print(''.join(ans))
