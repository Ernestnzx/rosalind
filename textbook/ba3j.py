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

with open('./testcase/rosalind_ba3j.txt','r') as f:
    k,d = map(int,f.readline().split())
    al,in_deg,out_deg = {},Counter(),Counter()
    for s in f.readlines():
        a,b = s.strip().split('|')
        u,v = (a[:-1],b[:-1]),(a[1:],b[1:])
        if u not in al: al[u] = []
        if v not in al: al[v] = []
        al[u].append(v)
        in_deg[v]+=1; out_deg[u]+=1
    s = next(iter(filter(lambda x: out_deg[x] - in_deg[x] == 1, in_deg.keys() | out_deg.keys())), 0)
    e = hierholzer(s,al)
    assert(len(e)-1 == sum(len(al[u]) for u in al)) 
    a,b = zip(*e); n = len(e)
    print(a[0] + ''.join(a[i][-1] for i in range(1,n)) + ''.join(b[i][-1] for i in range(n-d-k,n)))
 