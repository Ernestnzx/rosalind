from collections import *

def cyclospectrum(peptides):
    n,pm = len(peptides),sum(peptides)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] += prefix[i] + peptides[i]
    spectrum = Counter([0,pm])
    for i in range(1,n):
        for j in range(i+1,n+1):
            spectrum[prefix[j]-prefix[i]] += 1
            spectrum[pm-(prefix[j]-prefix[i])] += 1
    return spectrum

def score(p,s):
    p = cyclospectrum(p)
    return (p&s).total()

def trim(leaderboard,spectrum,n):
    global mass_table
    linear_scores = [
        (score(peptide,spectrum),i)
        for i,peptide in enumerate(leaderboard)
    ]
    linear_scores = sorted(linear_scores,key=lambda x : -x[0])
    leaderboard = [leaderboard[i] for s,i in linear_scores]
    for j in range(n,len(leaderboard)):
        if linear_scores[j] < linear_scores[n-1]:
            return leaderboard[:j]
    return leaderboard

def expand(peptides):
    global mass_table
    expanded_peptides = []
    for p in peptides:
        for t in mass_table:
            expanded_peptides.append(p+(t,))
    return tuple(expanded_peptides)

def sequencing(spectrum,n):
    leaderboard,leader_peptide,parent_mass = [()],(),max(spectrum)
    while leaderboard:
        leaderboard = expand(leaderboard)
        remove_peptide = set()
        for peptide in leaderboard:
            peptide_mass = sum(peptide)
            if peptide_mass == parent_mass:
                if score(peptide,spectrum) > score(leader_peptide,spectrum):
                   leader_peptide = peptide
            elif peptide_mass > parent_mass:
                remove_peptide.add(peptide)
        leaderboard = trim([x for x in leaderboard if x not in remove_peptide],spectrum,n)
    return leader_peptide

with open('./testcase/rosalind_ba4i.txt','r') as f:
    m = int(f.readline()); n = int(f.readline())
    s = list(map(int,f.readline().split()))
    c = Counter([s[i]-s[j] for i in range(1,len(s)) for j in range(i) if 57 <= s[i]-s[j] <= 200]).most_common()
    mass_table = c[:m]
    for i in range(m,len(c)):
        if c[i][1] < c[m-1][1]:
            mass_table.extend(c[m:i])
            break
    mass_table = [*map(lambda x:x[0],mass_table)]
    print('-'.join(map(str,sequencing(Counter(s),n))))
