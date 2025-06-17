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

with open('./testcase/rosalind_ba4g.txt','r') as f:
    n = int(f.readline())
    spectrum = Counter(map(int,f.readline().split()))
    mass_table = {
        int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    }
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
    print('-'.join(map(str,leader_peptide)))
