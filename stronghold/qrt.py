with open('./testcase/rosalind_qrt.txt','r') as f:
    am = f.readline().strip().split()
    ctbl = [s.strip() for s in f.readlines()]
    ans = set()
    for s in ctbl:
        c,d = [],[]
        for i,j in enumerate(s):
            if j == '0': c.append(i)
            if j == '1': d.append(i)
        if len(c) < 2 or len(d) < 2: continue
        n,m = len(c),len(d)
        for i in range(n-1):
            for j in range(i+1,n):
                for k in range(m-1):
                    for l in range(k+1,m):
                        w,x,y,z = c[i],c[j],d[k],d[l]
                        if w > x : w,x=x,w
                        if y > z : y,z=z,y
                        if (w,x) > (y,z): w,x,y,z=y,z,w,x
                        ans.add(((w,x,y,z)))
print(*sorted(map(lambda x : f'{{{am[x[0]]}, {am[x[1]]}}} {{{am[x[2]]}, {am[x[3]]}}}', ans)),sep='\n')
