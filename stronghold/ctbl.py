import re
with open('./testcase/rosalind_ctbl.txt','r') as f:
    s,ls,ans = eval(re.sub(r'([A-Za-z0-9_]+)',r'"\1"',f.readline().strip()[:-1])),[],[]
    def get_list(s):
        if isinstance(s,str):
            ls.append(s)
            return
        for i in s: get_list(i)

    def form_ctbl(s):
        if isinstance(s,str):
            return 1<<ls[s]
        mask = 0
        for i in s: mask |= form_ctbl(i)
        if mask == (1<<n)-1: return mask
        ans.append(''.join(str(mask>>i&1)for i in range(n)))
        return mask

    get_list(s)
    ls = {v:i for i,v in enumerate(sorted(ls))}; n = len(ls)
    form_ctbl(s)
    print(*sorted(ans),sep='\n')
