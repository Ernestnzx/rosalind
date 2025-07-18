def neighbor_joining(d,n,m):
    if n == 2:
        return [(i,j,d[i][j]) for i in d for j in d if i != j]
    td = {i : sum(map(lambda x:x[1],d[i].items())) for i in d}
    d_star,pos,min_val = {},(-1,-1),float('inf')
    for i in d:
        for j in d:
            if i != j:
                d_star.setdefault(i,{})[j] = (n-2)*d[i][j]-td[i]-td[j]
                if d_star[i][j] < min_val:
                    min_val = d_star[i][j]
                    pos = (i,j)
            else: d_star.setdefault(i,{})[j] = 0
    i,j = pos; delta = (td[i]-td[j])/(n-2)
    limb_i,limb_j = 0.5*(d[i][j]+delta),0.5*(d[i][j]-delta)
    d[m] = {k:0.5*(d[k][i]+d[k][j]-d[i][j]) for k in d}
    for k in d: d[k][m] = 0.5*(d[k][i]+d[k][j]-d[i][j]) if k != m else 0
    d.pop(i); d.pop(j);
    for k,v in d.items():
        if i in v: d[k].pop(i)
        if j in v: d[k].pop(j)
    t = neighbor_joining(d,n-1,m+1)
    t.append((m,i,limb_i)); t.append((i,m,limb_i))
    t.append((m,j,limb_j)); t.append((j,m,limb_j))
    return t

with open('./testcase/rosalind_ba7e.txt','r') as f:
    n,d = int(f.readline()),[list(map(int,line.split())) for line in f.readlines()]
    matrix = {}
    for i in range(n):
        for j in range(n):
            matrix.setdefault(i,{})[j] = matrix.setdefault(j,{})[i] = d[i][j]
    print('\n'.join(f'{u}->{v}:{w:.3f}' for u,v,w in sorted(neighbor_joining(matrix,n,n))),sep='\n')
