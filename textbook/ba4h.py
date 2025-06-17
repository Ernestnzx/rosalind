from collections import *

with open('./testcase/rosalind_ba4h.txt','r') as f:
    s = sorted(list(map(int,f.readline().split())))
    c = Counter([s[i]-s[j] for i in range(1,len(s)) for j in range(i)])
    ans = sorted([(v,k) for k,v in c.items()],key=lambda x : -x[0])
    print(*[' '.join([str(s) for _ in range(i)]) for i,s in ans if s != 0])
