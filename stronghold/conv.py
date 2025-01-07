with open('./testcase/rosalind_conv.txt','r') as f:
    s1 = list(map(lambda x : round(100000*float(x)), f.readline().split()))
    s2 = list(map(lambda x : round(100000*float(x)), f.readline().split()))
    d,max_v,ans = {},0,0
    for i in s1:
        for j in s2:
            if i-j not in d: d[i-j]=1
            else: d[i-j]+=1
    for k,v in d.items():
        if v > max_v:
            max_v,ans = v,k/100000
    print(max_v,ans)