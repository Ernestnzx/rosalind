with open('./testcase/rosalind_ba2h.txt','r') as f:
    p = f.readline().strip();
    dna = [s for s in f.readline().strip().split()];
    k,d = len(p),0
    for s in dna:
        hd = 10**9
        for kmer in [s[i:i+k] for i in range(len(s)-k+1)]:
            hd = min(hd,sum(a!=b for a,b in zip(p,kmer)))
        d += hd
    print(d)
