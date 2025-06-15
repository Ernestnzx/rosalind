from collections import *

def hierholzer(s,al):
    ans,idx,st = [],[0]*(max(al)+1),[s]
    while len(st) != 0:
        u = st[-1]
        if idx[u] < len(al[u]):
            st.append(al[u][idx[u]])
            idx[u] += 1
        else:
            ans.append(u)
            st.pop()
    ans = ans[::-1]
    return ans

with open('./testcase/rosalind_ba3g.txt','r') as f:
    al = {}
    for s in f.readlines():
        u,v = s.split('->')
        al[int(u)] = list(map(int,v.split(',')))
        for v in al[int(u)]:
            if v not in al: al[v] = []
    in_deg,out_deg = Counter(), Counter()
    for u,neigh in al.items():
        for v in neigh:
            in_deg[v] += 1; out_deg[u] += 1
    s = next(iter(filter(lambda x: out_deg[x] - in_deg[x] == 1, in_deg.keys() | out_deg.keys())), 0)
    e = hierholzer(s,al)
    assert(len(e)-1 == sum(len(al[u]) for u in al)) 
    print('->'.join(map(str,e)))
    