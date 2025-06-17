from Bio.Seq import Seq
with open('testcase/rosalind_ba4b.txt','r') as f:
    dna = f.readline().strip(); p = f.readline().strip()
    n,m,ans = len(dna),len(p),[]

    def find_matches(seq,p):
        ans = []
        for i in range(3):
            temp = seq[i:n-((3-i)%3)]
            for j in range(0,len(temp)-3*m+1,3):
                s = Seq(temp[j:j+3*m])
                if s.translate() == p: ans.append(s)
        return ans
    
    print(*sorted(find_matches(Seq(dna),p) + find_matches(Seq(dna).reverse_complement(),p)),sep='\n')
