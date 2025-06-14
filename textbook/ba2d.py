from collections import Counter

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
    profile = {'A':[0]*k,'C':[0]*k,'G':[0]*k,'T':[0]*k}
    for i in range(m):
        counts = Counter(motif[i] for motif in motifs)
        for b in 'ACGT': profile[b][i] = counts[b] / len(motifs)
    return profile
        
def greedy_motif_search(dna,k,t):
    n,best_motifs = len(dna[0]),[dna[i][:k] for i in range(t)]
    for motif in [dna[0][i:i+k] for i in range(n-k+1)]:
        motif_1 = motif
        motifs = [motif_1]
        for i in range(1,t):
            curr_profile = build_profile(motifs)
            motifs.append(most_probable_string(curr_profile,dna[i],k))
        if score(motifs) < score(best_motifs): best_motifs = motifs
    return best_motifs

with open('./testcase/rosalind_ba2d.txt','r') as f:
    k,t = map(int,f.readline().split())
    dna = [s.strip() for s in f.readlines()]
    print(*greedy_motif_search(dna,k,t),sep='\n')
