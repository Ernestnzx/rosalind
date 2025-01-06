with open('./testcase/rosalind_rstr.txt','r') as f:
    n,x=map(float,f.readline().split())
    s=f.readline().strip()
gc,at,prob=x/2,(1-x)/2,1
for c in s: prob *= gc if c=='C' or c=='G' else at
print(round(1-(1-prob)**n,3)) #Pr[X>=1] = Pr[X=0]
