from collections import *
from random import *

def score(motifs):
    return sum(
        len(motifs)-Counter(motif[i] for motif in motifs).most_common(1)[0][1]
        for i in range(len(motifs[0]))
    )

def most_probable_string(profile,dna,k):
    max_p,ans = -1,''
    for i in range(len(dna)-k+1):
        p = 1
        for j,c in enumerate(dna[i:i+k]):
            p *= profile[c][j]
        if max_p < p: max_p,ans=p,dna[i:i+k]
    return ans

def build_profile(motifs):
    m = len(motifs[0])
    profile = {'A':[1]*k,'C':[1]*k,'G':[1]*k,'T':[1]*k}
    for i in range(m):
        counts = Counter(motif[i] for motif in motifs)
        for b in 'ACGT': profile[b][i] = (counts[b] + 1) / (len(motifs)+4)
    return profile

def randomized_motif_search(dna,k,t):
    n,best_motifs = len(dna[0]),[]
    for s in dna:
        i = randint(0,n-k)
        best_motifs.append(s[i:i+k])
    motifs = [s for s in best_motifs]
    while True:
        profile = build_profile(motifs)
        motifs = [most_probable_string(profile,s,k) for s in dna]
        if score(motifs) < score(best_motifs):
            best_motifs = [s for s in motifs]
        else:
            return best_motifs

with open('./testcase/rosalind_ba2f.txt','r') as f:
    k,t = map(int,f.readline().split())
    dna = [s.strip() for s in f.readlines()]
    best_motif,best_score = [],10**9
    for _ in range(1000):
        motifs = randomized_motif_search(dna,k,t)
        motif_score = score(motifs)
        if motif_score < best_score:
            best_motif,best_score = motifs,motif_score
    print(*best_motif,sep='\n')
