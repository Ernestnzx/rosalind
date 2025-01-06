with open('./testcase/rosalind_eval.txt','r') as f:
    n = int(f.readline())
    s = f.readline().strip()
    a = list(map(float,f.readline().split()))
for x in a:
    gc,at,prob = x/2,(1-x)/2,1
    for c in s:
        prob *= gc if c=='G' or c=='C' else at
    print(f'{(n-len(s)+1)*prob:.3f}')
