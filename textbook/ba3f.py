def hierholzer(s,al):
    ans,idx,st = [],[0]*len(al),[s]
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

with open('./testcase/rosalind_ba3f.txt','r') as f:
    al = {}
    for s in f.readlines():
        u,v = s.split('->')
        al[int(u)] = list(map(int,v.split(',')))
    eulerian = hierholzer(0,al)
    assert(len(eulerian)-1 == sum(len(al[u]) for u in al))
    print('->'.join(map(str,eulerian)))