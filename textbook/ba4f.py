from collections import Counter

def cyclospectrum(peptides):
    n,pm = len(peptides),sum(mass_table[c] for c in peptides)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] += prefix[i] + mass_table[peptides[i]]
    spectrum = Counter([0,pm])
    for i in range(1,n):
        for j in range(i+1,n+1):
            spectrum[prefix[j]-prefix[i]] += 1
            spectrum[pm-(prefix[j]-prefix[i])] += 1
    return spectrum

with open('./testcase/rosalind_ba4f.txt','r') as f:
    p = f.readline().strip()
    s = Counter(map(int,f.readline().split()))
    mass_table = {
        i.split()[0] : int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    }
    p = cyclospectrum(p)
    print((s&p).total())