from collections import Counter

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

def is_consistent(peptides,spectrum):
    n = len(peptides); prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] += prefix[i] + peptides[i]
    linear_spectrum = Counter()
    for i in range(n):
        for j in range(i+1,n+1):
            linear_spectrum[prefix[j]-prefix[i]] += 1
    return not linear_spectrum-spectrum

def cyclopeptide_sequencing(peptides,spectrum,parent_mass):
    global mass_table
    total_weight = sum(peptides)
    if total_weight >= parent_mass:
        return ['-'.join(map(str,peptides))] \
            if total_weight == parent_mass and \
                cyclospectrum(peptides) == Counter(spectrum) else []
    ans = []
    for peptide in mass_table:
        peptides.append(peptide)
        if is_consistent(peptides,spectrum):
            ans.extend(cyclopeptide_sequencing(peptides,spectrum,parent_mass))
        peptides.pop()
    return ans

with open('./testcase/rosalind_ba4e.txt','r') as f:
    s = Counter(map(int,f.readline().split()))
    mass_table = {
        int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    }
    print(*cyclopeptide_sequencing([],s,max(s)))
