class LinkNode(object):
    def __init__(self, data):
        self.data = data
        self.node =None

class Link(object):
    def __init__(self, l = None):
        if l == None:
            self.data = None
            pass;
        else:   
            self.head = LinkNode(l[0])
            t = self.head            
            for i in l[1:]:
                t.node = LinkNode(i)
                t = t.node

    def __len__(self):
        n = self.head
        c = 0
        while n is not None:
            c += 1
            n = n.node
        return c

    def printl(self):
        n = self.head
        while n is not None:
            print n.data
            n = n.node

    def append(self, data):
        if self.head is not None:
            n = self.head
            while n.node is not None:
                n = n.node
            n.node = LinkNode(data)
        else:
            self.head = LinkNode(data)
      
    def find(self, data):
        n = self.head
        f = False
        while n is not None:
            if n.data == data:
                f = True
                break
            n = n.node
        if f == True:
            return n
        else:
            return None

    def insert(self, node, data):
        n = self.head
        f = False
        while n is not None:
            if n == node:
                f = True
                break
            n = n.node
        if f == False:
            return False

        m = LinkNode(data)
        if n.node is not None:
            m.node = n.node.node
        n.node = m
        return True

    def remove(self, node):
        n = self.head
        if n == node:
            self.head = n.node
            return True

        while n.node is not None:
            if n.node == node:
                break
            n = n.node
        if n.node is None:
            return False
        n.node = n.node.node
        return True

    def invert(self):
        t = m = None
        while self.head is not None:
            t = m
            m = self.head
            self.head = self.head.node
            m.node = t
        self.head = m
