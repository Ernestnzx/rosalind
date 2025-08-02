class Node:
    def __init__(self,id):
        self.neigh = {}
        self.id = id
        self.is_word = 0

class Trie:
    def __init__(self,patterns):
        self.root = Node(0)
        self.size = 1
        self.suffix_branch = []
        for pattern in patterns:
            curr = self.root
            for c in pattern:
                if c not in curr.neigh:
                    curr.neigh[c] = Node(self.size)
                    self.size += 1
                curr = curr.neigh[c]
            curr.is_word = 1

    def traverse(self, u=None, path=[]):
        if not u: u = self.root
        if len(u.neigh) != 1:
            if path: self.suffix_branch.append(''.join(path))
            path = []
        for c,v in u.neigh.items():
            self.traverse(v,path+[c])

    def matching(self,text):
        n,pos = len(text),[]
        for i in range(n):
            s,idx,is_found = text[i:],0,0
            c,u = s[idx],self.root
            while not is_found:
                if not u.neigh: is_found = 1
                elif c in u.neigh:
                    if idx+1<len(s): idx += 1
                    c,u = s[idx],u.neigh[c]
                else: is_found = 0; break
            if is_found: pos.append(i)
        return pos

with open('./testcase/rosalind_ba9c.txt','r') as f:
    text = f.readline().strip()
    t = Trie([text[i:] for i in range(len(text))]); t.traverse()
    print(*sorted(t.suffix_branch),sep='\n')
