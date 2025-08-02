with open('./testcase/rosalind_ba9r.txt','r') as f:
    s = f.readline().strip()
    sa = list(eval(f.readline()))
    lcp = list(eval(f.readline()))
    suffix_tree,st,edges,count = {0:set()},[(0,0)],{0:''},1
    for i,idx in enumerate(sa):
        lcp_val = lcp[i]
        while st[-1][1] > lcp_val: st.pop()
        parent,depth = st[-1]

        if depth == lcp_val:
            suffix_tree.setdefault(parent,set()).add(count)
            suffix_tree.setdefault(count,set())
            edges[count] = s[idx+lcp_val:]
            st.append((count,lcp_val))
            count += 1
        elif depth < lcp_val:
            # breaking up the previous edge
            edges[parent] = s[sa[i-1]:sa[i-1]+lcp_val-depth]
            suffix_tree.setdefault(parent,set()).add(count);
            suffix_tree.setdefault(count,set())
            edges[count] = s[sa[i-1]+lcp_val-depth:]
            count += 1
            st.append((count,depth))
            # adding the new edge
            suffix_tree.setdefault(parent,set()).add(count);
            suffix_tree.setdefault(count,set())
            edges[count] = s[idx+lcp_val-depth:]
            count += 1
            st.append((count,lcp_val))
        else:
            assert(True)
    # Result is wrong, will get back to it.
    print(*[edges[k] for k in suffix_tree],sep='\n')
