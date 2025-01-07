with open('./testcase/rosalind_lrep.txt','r') as f:
    s = f.readline().strip()
    k = int(f.readline())
    al = {} # The suffix tree!
    for line in f.readlines():
        u,v,pos,l = line.strip().split()
        u,v,pos,l = int(u[4:]),int(v[4:]),int(pos)-1,int(l)
        if u not in al: al[u] = []
        if v not in al: al[v] = []
        al[u].append((v,pos,l))
    max_len,substr = 0,()
    def traverse(u,d,p):
        global max_len, substr
        if not len(al[u]): return 1
        count = 0
        for v,pos,l in al[u]:
            count += traverse(v,d+l,p+((pos,l),))
        if count >= k and d > max_len:
            max_len,substr = d,p
        return count 
    traverse(1,0,())
    ans = ''
    for pos,l in substr:
        ans += s[pos:pos+l]
    print(ans)