import re
with open('./testcase/rosalind_sptd.txt','r') as f:
    am = {s : i for i,s in enumerate(f.readline().strip().split())}
    t1 = eval(re.sub(r'([A-Za-z0-9_]+)',r'"\1"',f.readline().strip()[:-1]))
    t2 = eval(re.sub(r'([A-Za-z0-9_]+)',r'"\1"',f.readline().strip()[:-1]))

    def form_ctbl(s,ans):
        if isinstance(s,str):
            return 1<<am[s]
        mask = 0
        for i in s: mask |= form_ctbl(i,ans)
        if mask == (1<<n)-1: return mask
        ans.add(mask)
        return mask
    
    n,s1,s2 = len(am),set(),set()
    form_ctbl(t1,s1)
    form_ctbl(t2,s2)
    print(2*(n-3)-2*len(s1&s2))
