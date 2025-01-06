with open('./testcase/rosalind_gc.txt','r') as f:
    d,key = {},''
    while line:=f.readline().strip():
        if line[0] == '>': d[key:=line] = ''
        else: d[key]+= line
    name,ans='',0
    for k,v in d.items():
        count = v.count('G')+v.count('C')
        calc = 100*count/len(v)
        if ans < calc: name,ans=k,calc
    print(f'{name[1:]}\n{ans:.6f}')
