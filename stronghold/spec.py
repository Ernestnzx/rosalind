with open('./testcase/mass_table.txt') as f1:
    d = {}
    for line in f1.readlines():
        k,v=line.split()
        d[round(float(v)*1000)] = k
with open('./testcase/rosalind_spec.txt','r') as f2:
    a,ans = list(map(float,f2.readlines())),''
    for i in range(1,len(a)):
        ans += d[round((a[i]-a[i-1])*1000)]
    print(ans)