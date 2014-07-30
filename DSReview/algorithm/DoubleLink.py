class DoubleLinkNode(object):
    def __init__(self, data=None):
        self.data = data
        self.front = None
        self.back = None

class DoubleLink(object):
    def __init__(self, l=None):
        if l == None:
            self.data = DoubleLinkNode()
            pass
        else:   
            self.head = DoubleLinkNode()
            t = self.head
            for i in l:
                n = DoubleLinkNode(i)
                t.front = n
                n.back = t
                t = n
            t.front = self.head
            self.head.back = t

    def __len__(self):
        n = self.head.front
        c = 0
        while n.data is not None:
            c += 1
            n = n.front
        return c

    def printl(self):
        n = self.head.front
        while n.data is not None:
            print n.data
            n = n.front
        n = self.head.back
        while n.data is not None:
            print n.data
            n = n.back

    def append(self, data):
        if self.head.front.data is not None:
            n = self.head.back            
            n.front = DoubleLinkNode(data)
            n.front.back = n
            n.front.front = self.head
            self.head.back = n.front
        else:
            self.head.front = DoubleLinkNode(data)
            self.head.back = self.head.front
            self.head.front.back = self.head
            self.head.front.front = self.head
      
    def find(self, data):
        n = self.head.front
        f = False
        while n.data is not None:
            if n.data == data:
                f = True
                break
            n = n.front
        if f == True:
            return n
        else:
            return None

    def insert(self, node, data):
        n = self.head.front
        f = False
        while n.data is not None:
            if n == node:
                f = True
                break
            n = n.front
        if f == False:
            return False

        m = DoubleLinkNode(data)
        m.back = n
        n.front.back = m
        m.front = n.front
        n.front = m        
        return True

    def remove(self, node):
        n = self.head.front
        if n == node:
            self.head.front = self.head.front.front
            n.front.back = self.head
            return 
        while n.data is not None:
            if n.front == node:
                break
            n = n.front
        if n.data is None:
            return False
        n.front.front.back = n
        n.front = n.front.front
        return True

    def invert(self):
        n = self.head.front
        while n.data is not None:
            t = n.front
            n.front = n.back
            n.back = t
            n = n.back          
        t = self.head.front
        self.head.front = self.head.back  
        self.head.back = t