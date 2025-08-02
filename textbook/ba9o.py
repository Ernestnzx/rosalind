def hd(a,b): return sum(i!=j for i,j in zip(a,b))

with open('./testcase/rosalind_ba9o.txt','r') as f:
    s = f.readline().strip()
    q = [t.strip() for t in f.readline().split()]
    d,n = int(f.readline()),len(s)
    # naive approach (O(|s|*q*|t|)), will do efficient method soon
    print(*sorted([i for t in q for i in range(n-len(t)+1) if hd(s[i:i+len(t)],t) <= d]))