with open('./testcase/rosalind_ba3b.txt','r') as f:
    dna = [s.strip() for s in f.readlines()]
    print(dna[0] + ''.join(dna[i][-1] for i in range(1,len(dna))))