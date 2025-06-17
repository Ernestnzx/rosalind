from collections import *

def linear_spectrum(peptides):
    global mass_table
    n = len(peptides); prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] += prefix[i] + mass_table[peptides[i]]
    linear_spectrum = [0]
    for i in range(n):
        for j in range(i+1,n+1):
            linear_spectrum.append(prefix[j]-prefix[i])
    return Counter(linear_spectrum)

def linear_score(p,s):
    p = linear_spectrum(p)
    return (p&s).total()

def trim(leaderboard,spectrum,n):
    global mass_table
    linear_scores = [
        (linear_score(peptide,spectrum),i)
        for i,peptide in enumerate(leaderboard)
    ]
    linear_scores = sorted(linear_scores,key=lambda x : -x[0])
    leaderboard = [leaderboard[i] for s,i in linear_scores]
    for j in range(n,len(leaderboard)):
        if linear_scores[j] < linear_scores[n-1]:
            return leaderboard[:j]
    return leaderboard


with open('./testcase/rosalind_ba4l.txt','r') as f:
    leaderboard = f.readline().strip().split()
    spectrum = Counter(map(int,f.readline().split()))
    n = int(f.readline())
    mass_table = {
        i.split()[0] : int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    }
    print(*trim(leaderboard,spectrum,n))
