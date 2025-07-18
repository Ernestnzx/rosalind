def d(x,y): return 0 if x == y else 1

def small_parsimony(t,character,topo,alphabet='ACGT'):
    s = [[float('inf') for _ in alphabet] for _ in t] 
    for u in t:
        if u in character:
            for i,k in enumerate(alphabet):
                if character[u] == k:
                    s[u][i] = 0
    m,backtrack = len(alphabet),[{} for _ in t]
    for u in topo:
        if not t[u]: continue
        l,r = t[u]
        for i,k in enumerate(alphabet):
            min_left_score = min_right_score = float('inf')
            left_idx,right_idx = -1,-1
            for j in range(m):
                if min_left_score > s[l][j]+d(alphabet[j],k):
                    min_left_score = s[l][j]+d(alphabet[j],k)
                    left_idx = j
                if min_right_score > s[r][j]+d(alphabet[j],k):
                    min_right_score = s[r][j]+d(alphabet[j],k)
                    right_idx = j
            s[u][i] = min_left_score+min_right_score
            backtrack[u][i] = (left_idx,right_idx)
    return (s,backtrack)

def reconstruct(t,s,backtrack,root,alphabet='ACGT'):
    m = len(alphabet)
    assignment = [None] * len(t)
    def dfs(u,parent_char=None):
        if parent_char is None: assignment[u] = min(range(m),key=lambda i:s[u][i])
        else: assignment[u] = min(range(m),key=lambda i:s[u][i]+d(i,parent_char))
        if u in t and len(t[u]) == 2:
            l,r = t[u]
            li,ri = backtrack[u][assignment[u]]
            dfs(l,li)
            dfs(r,ri)
    dfs(root)
    return assignment

def g(t,dna,topo,root):
    m = len(next(iter(dna)))
    total_score,seq = 0,['']*len(t)
    for i in range(m):
        character = {j:s[i] for j,s in enumerate(dna)}
        s,bt = small_parsimony(t,character,topo)
        a = reconstruct(t,s,bt,root)
        for u in range(len(t)):
            seq[u] += character[u] if u < len(dna) else 'ACGT'[a[u]]
        total_score += min(s[root])
    return total_score,seq

# Still not too sure what's wrong here, will pass this question for now
with open('./testcase/temp.txt','r') as f:
    n,t,dna = int(f.readline()),{},{}
    for _ in range(2*n):
        u,v = f.readline().strip().split('->')
        if u.isalpha():
            dna.setdefault(u,len(dna))
            u,v = dna[u],int(v)
        elif v.isalpha():
            dna.setdefault(v,len(dna))
            u,v = int(u),dna[v]
        else:
            u,v = int(u),int(v)
        t.setdefault(u,[]).append(v)
    edge = (-1,-1)
    for s in f.readlines():
        u,v = map(int,s.strip().split('->'))
        t.setdefault(u,[]).append(v)
        edge = (u,v)
    root,vis,order = len(t),set(),[]
    t[u].remove(v); t[v].remove(u)
    t.setdefault(root,[]).append(u); t[u].append(root)
    t.setdefault(root,[]).append(v); t[v].append(root)
    def topo(u):
        vis.add(u)
        for v in t[u]:
            if v not in vis:
                topo(v)
        order.append(u)
    topo(root);
    order,rooted_tree,vis = order[::-1],{},set()
    for u in order:
        for v in t[u]:
            if v in vis: continue
            rooted_tree.setdefault(u,[]).append(v)
            rooted_tree.setdefault(v,[])
        vis.add(u)
    score,seq = g(rooted_tree,dna,order,root)
    print(score)
    for u,neigh in t.items():
        for v in neigh:
            w = sum(seq[u][i]!=seq[v][i] for i in range(len(dna[0])))
            print(f'{seq[u]}->{seq[v]}:{w}')
            print(f'{seq[v]}->{seq[u]}:{w}')
