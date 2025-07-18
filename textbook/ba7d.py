def dist(c1,c2,d):
    return sum(d[i][j] for i in c1 for j in c2) / (len(c1) * len(c2))

def upgma(d,n):
    clusters,t,age,matrix,mapping = [],{},{},{},{}
    for i in range(n):
        age[(i,)] = 0
        clusters.append((i,))
        t.setdefault((i,),[])
        mapping[(i,)] = i
    for i in range(n):
        for j in range(n):
            matrix.setdefault((i,),{})[(j,)] = d[i][j]
    while len(clusters) > 1:
        idx,min_dist = (-1,-1),10**9
        for i,c1 in enumerate(clusters):
            for j,c2 in enumerate(clusters):
                if i <= j: continue
                calc = dist(c1,c2,d)
                if calc < min_dist:
                    idx,min_dist = (i,j),calc
        ci,cj = clusters[idx[0]],clusters[idx[1]]
        c_new = ci+cj; mapping[c_new] = len(mapping)
        age[c_new] = dist(ci,cj,d)/2
        t.setdefault(c_new,[]).append(ci); t[ci].append(c_new)
        t.setdefault(c_new,[]).append(cj); t[cj].append(c_new)
        matrix.pop(ci); matrix.pop(cj)
        for k,v in matrix.items():
            if ci in v: v.pop(ci)
            if cj in v: v.pop(cj)
        clusters.pop(idx[0]); clusters.pop(idx[1])
        for i,c in enumerate(clusters):
            val = dist(c_new,c,d)
            matrix.setdefault(c_new,{})[c] = matrix.setdefault(c,{})[c_new] = val
        clusters.append(c_new)
    return set((mapping[u],mapping[v],abs(age[u]-age[v])) for u,neigh in t.items() for v in neigh)

with open('./testcase/rosalind_ba7d.txt','r') as f:
    n,d = int(f.readline()),[list(map(int,line.split())) for line in f.readlines()]
    print('\n'.join(f'{u}->{v}:{w:.3f}' for u,v,w in sorted(upgma(d,n))))
