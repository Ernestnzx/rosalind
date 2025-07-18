from collections import *
with open('./testcase/rosalind_ba7a.txt','r') as f:
    n,al,order = int(f.readline()),{},Counter()
    for s in f.readlines():
        u,p = s.strip().split('->'); u = int(u)
        v,w = map(int,p.split(':'))
        al.setdefault(u,[]).append((v,w))
        order[u] += 1; order[v] += 1
    leaves = set([i for i in range(len(al)) if order[i] == 2])
    assert len(leaves) == n
    # Can use DFS + LCA to compute dij by dist[i] + dist[j] - 2*dist[LCA(i,j)]
    # But since O(n^2) is still needed, running DFS for all leaves is just as fast.
    ans = []
    for u in leaves:
        dist = [-1]*len(al); dist[u] = 0
        def dfs(u):
            for v,w in al[u]:
                if dist[v] == -1:
                   dist[v] = dist[u] + w
                   dfs(v)
        dfs(u)
        ans.append([dist[i] for i in range(len(al)) if i in leaves])
    print('\n'.join(' '.join(map(str,i)) for i in ans))
