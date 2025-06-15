from collections import *

def hierholzer(s,al):
    ans,idx,st = [],{},[s]
    while len(st) != 0:
        u = st[-1]
        if u not in idx: idx[u] = 0
        if idx[u] < len(al[u]):
            st.append(al[u][idx[u]])
            idx[u] += 1
        else:
            ans.append(u)
            st.pop()
    ans = ans[::-1]
    return ans

with open('./testcase/rosalind_ba3i.txt','r') as f:
    k,al = int(f.readline()),{}
    for b in [f'{i:0{k}b}' for i in range(1<<k)]:
        u,v = b[:-1],b[1:]
        if u not in al: al[u] = []
        if v not in al: al[v] = []
        al[u].append(v)
    e = hierholzer(next(iter(al)),al)
    ans = e[0] + ''.join(e[i][-1] for i in range(1,len(e)))
    assert len(set(ans[i:i+k] for i in range(len(ans)-k+1))) == 1<<k
    print(ans[:1<<k])
