with open('./testcase/rosalind_ba1e.txt','r') as f:
    s = f.readline().strip();
    k,l,t = map(int,f.readline().split())
    n,kmer,ans = len(s),{},set()
    for i in range(l-k+1):
        u = s[i:i+k]
        if u not in kmer: kmer[u] = 0
        kmer[u] += 1
    ans.update(k for k,v in kmer.items() if v >= t)
    for i in range(1,n-l+1):
        a,b = s[i-1:i+k-1],s[i+l-k:i+l]
        if b not in kmer: kmer[b] = 0
        kmer[a] -= 1; kmer[b] += 1
        if kmer[b] >= t: ans.add(b)
    print(*ans)
