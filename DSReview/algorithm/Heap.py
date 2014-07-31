class Heap(object):
    def __init__(self, l=None):
        self.heap = []
        if l is not None:
            for i in l:
                self.insert(i)
        

    def insert(self, data):
        self.heap.append(None)
        i = len(self.heap)        
        while i != 1 and data > self.heap[i / 2 - 1]:
            self.heap[i - 1] = self.heap[i / 2 - 1]
            i /= 2
        self.heap[i - 1] = data

    def delete(self):
        if len(self.heap) == 0:
            return
        i = self.heap[0]
        t = self.heap[len(self.heap) - 1]
        self.heap.remove(self.heap[len(self.heap) - 1])       
        p = 1
        c = 2
        while c <= len(self.heap):
            if c < len(self.heap) and (self.heap[c - 1] < self.heap[c]):
                c +=1
            if t >= self.heap[c - 1]:
                break
            self.heap[p - 1] = self.heap[c - 1] 
            p = c
            c *= 2
        self.heap[p - 1] = t
        return i



