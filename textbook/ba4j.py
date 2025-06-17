def linear_spectrum(peptides):
    n = len(peptides); prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] += prefix[i] + mass_table[peptides[i]]
    linear_spectrum = [0]
    for i in range(n):
        for j in range(i+1,n+1):
            linear_spectrum.append(prefix[j]-prefix[i])
    return linear_spectrum

with open('./testcase/rosalind_ba4j.txt','r') as f:
    mass_table = {
        i.split()[0] : int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    }
    print(*sorted(linear_spectrum(f.readline().strip())))