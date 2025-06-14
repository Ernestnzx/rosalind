from collections import *
from random import *

def score(motifs):
    return sum(
        len(motifs)-Counter(motif[i] for motif in motifs).most_common(1)[0][1]
        for i in range(len(motifs[0]))
    )

def sample_string(profile,dna,k):
    probs,kmer = [],[]
    for i in range(len(dna)-k+1):
        p = 1
        for j,c in enumerate(dna[i:i+k]):
            p *= profile[c][j]
        probs.append(p); kmer.append(dna[i:i+k])
    return choices(kmer, weights=probs)[0]


def build_profile(motifs,skip=None):
    m = len(motifs[0])
    profile = {'A':[1]*m,'C':[1]*m,'G':[1]*m,'T':[1]*m}
    for i in range(m):
        counts = Counter(motif[i] for j,motif in enumerate(motifs) if j != skip)
        for b in 'ACGT':
            profile[b][i] = (counts[b] + 1) / (len(motifs)-(1 if skip is not None else 0)+4)
    return profile

def gibbs_sampler(dna,k,t,n):
    n,best_motifs = len(dna[0]),[]
    for s in dna:
        i = randint(0,n-k)
        best_motifs.append(s[i:i+k])
    motifs = [s for s in best_motifs]
    for _ in range(n):
        idx = randint(0,t-1)
        profile = build_profile(motifs,skip=idx)
        motifs[idx] = sample_string(profile,dna[idx],k)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]
    return best_motifs

with open('./testcase/temp.txt','r') as f:
    k,t,n = map(int,f.readline().strip().split())
    dna = [s.strip() for s in f.readlines()]
    best_motif,best_score = [],10**9
    for _ in range(50):
        motifs = gibbs_sampler(dna,k,t,n)
        motif_score = score(motifs)
        if motif_score < best_score:
            best_motif,best_score = motifs,motif_score
    print(*best_motif,sep='\n')
