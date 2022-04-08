class  Heap:
    def __init__(self):
        self.heap = []
        self.lh = len(self.heap)
    def get_parent(self, node):
        return node//2 - 1 
    def get_child(self, node):
        return (2*node - 1, 2*node)
    def swap(self,a,b):
        t = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = t
    def heapify_insert(self):
        c = len(self.heap) - 1
        while True:
            p = self.get_parent(c+1)
            if self.heap[p] > self.heap[c]:
                self.swap(p,c)
                c = p
            else:
                break
    def heapify_extract(self):
        c = 0
        while True:
            a,b = self.get_child(c+1)
            if a >= self.lh:
                break
            print('1:',self.heap, a,b,c)
            if self.heap[a]<self.heap[b] and self.heap[c]>self.heap[a]:
                self.swap(a,c)
                print('2:',self.heap, a,b,c)
                c = a
            elif self.heap[c]>self.heap[b]:
                self.swap(c,b)
                print('3:',self.heap, a,b,c)
                c = b
            else:
                break
    def insert(self, data):
        self.heap.append(data)
        self.heapify_insert()
    def extract_min(self):
        v = self.heap[0]
        length = len(self.heap)
        self.heap[0] = self.heap[length - 1]
        self.heapify_extract()
        return v 
    def view_min(self):
        return self.heap[0]

h = Heap()
h.insert(4)
h.insert(50)
h.insert(7)
h.insert(55)
h.insert(90)
h.insert(87)
print(h.view_min())
print(h.extract_min())


