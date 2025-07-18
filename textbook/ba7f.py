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

def reconstruct(t, s, backtrack, topo, alphabet='ACGT'):
    m = len(alphabet)
    assignment = [None] * len(t)
    def dfs(u, parent_char=None):
        if parent_char is None: assignment[u] = min(range(m),key=lambda i:s[u][i])
        else: assignment[u] = min(range(m),key=lambda i:s[u][i]+d(i,parent_char))
        if u in t and len(t[u]) == 2:
            l,r = t[u]
            li,ri = backtrack[u][assignment[u]]
            dfs(l,li)
            dfs(r,ri) 
    dfs(topo[-1])
    return assignment

def g(t,dna):
    m = len(dna[0])
    topo,vis = [],set()
    def dfs(u):
        vis.add(u)
        for v in t[u]:
            if v not in vis:
               dfs(v) 
        if u >= len(dna): topo.append(u)
    dfs(len(t)-1)
    total_score,seq = 0,['']*len(t)
    for i in range(m):
        character = {j:s[i] for j,s in enumerate(dna)}
        s,bt = small_parsimony(t,character,topo)
        a = reconstruct(t,s,bt,topo)
        for u in range(len(t)):
            seq[u] += character[u] if u < len(dna) else 'ACGT'[a[u]]
        total_score += min(s[topo[-1]])
    return total_score,seq

with open('./testcase/rosalind_ba7f.txt','r') as f:
    n = int(f.readline())
    t,dna = {},[]
    for i in range(n):
        a,b = f.readline().split('->')
        dna.append(b.strip())
        t.setdefault(int(a),[]).append(i)
        t.setdefault(i,[])
    for s in f.readlines():
        u,v = map(int,s.split('->'))
        t.setdefault(u,[]).append(v)
        t.setdefault(v,[])
    score,seq = g(t,dna)
    print(score)
    for u,neigh in t.items():
        for v in neigh:
            w = sum(seq[u][i]!=seq[v][i] for i in range(len(dna[0])))
            print(f'{seq[u]}->{seq[v]}:{w}')
            print(f'{seq[v]}->{seq[u]}:{w}')
