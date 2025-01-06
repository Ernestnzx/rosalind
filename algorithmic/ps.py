class Heap:
    def __init__(self):
        self.arr = [None]

    def push(self,val):
        self.arr.append(val)
        self.bubble_up(len(self.arr)-1)

    def pop(self):
        if self.is_empty(): return None
        self.arr[1],self.arr[-1]=self.arr[-1],self.arr[1]
        val=self.arr.pop()
        self.bubble_down(1)
        return val

    def bubble_up(self,i):
        if i == 1: return
        p=self.get_parent(i)
        if self.arr[p] > self.arr[i]:
            self.arr[p],self.arr[i]=self.arr[i],self.arr[p]
            self.bubble_up(p)

    def bubble_down(self,i):
        sid,l,r = i,self.get_left_child(i),self.get_right_child(i)
        if l < len(self.arr) and self.arr[i] > self.arr[l]: sid = l
        if r < len(self.arr) and self.arr[sid] > self.arr[r]: sid = r
        if i!=sid:
            self.arr[i],self.arr[sid]=self.arr[sid],self.arr[i]
            self.bubble_down(sid)

    def print_ds(self): print(self.arr)
    def get_parent(self,i): return i>>1
    def get_left_child(self,i): return i<<1
    def get_right_child(self,i): return (i<<1)|1
    def is_empty(self): return len(self.arr)==1

with open('./testcase/rosalind_ps.txt','r') as f:
    n=int(f.readline())
    a=list(map(int,f.readline().split()))
    k=int(f.readline())
    heap = Heap()
    for v in a: heap.push(v)
    for _ in range(k): print(heap.pop(),end=' ')
