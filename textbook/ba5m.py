def score(idx,arr):
    chars = ['-' if idx[i] == 0 else arr[i][idx[i]-1] for i in range(len(idx))]
    return 1 if all(c == chars[0] for c in chars) else 0

def multiple_alignment(dna,dp,t=()):
    if len(dna) == len(t):
        for i in range(1,1<<len(t)):
            ts = [i>>y&1 for y in range(len(t))]
            r = tuple(t[i]-ts[i] for i in range(len(t)))
            if any(i < 0 for i in r): continue
            prev,curr = dp.get(r,-10**9),dp.get(t,-10**9)
            sc = score([t[j] if ts[j] else 0 for j in range(len(t))], dna)
            dp[t]=max(curr,prev+sc)
        return
    for i in range(len(dna[len(t)])+1):
        multiple_alignment(dna,dp,t+(i,))

def get_alignment(dna,dp):
    s,t,align = tuple(0 for _ in dna),tuple(len(s) for s in dna),[[] for _ in dna]
    while s != t:
        for x in range(1,1<<len(dna)):
            ts = [x>>y&1 for y in range(len(dna))]
            u = tuple(t[i]-ts[i] for i in range(len(t)))
            if any(i < 0 for i in u): continue
            if dp[t] == dp[u] + score([t[j] if ts[j] else 0 for j in range(len(t))], dna):
                for i in range(len(dna)):
                    align[i].append('-' if ts[i] == 0 else dna[i][t[i]-ts[i]])
                t = u
    return [''.join(i[::-1]) for i in align]

with open('./testcase/rosalind_ba5m.txt','r') as f:
    dna = [s.strip() for s in f.readlines()]
    dp = {}; dp[tuple([0]*len(dna))] = 0
    multiple_alignment(dna,dp)
    print(dp[tuple(len(s) for s in dna)],*get_alignment(dna,dp),sep='\n')
