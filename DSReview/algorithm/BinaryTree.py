class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, l=None):
        def init(b, l, i):
            if i >= len(l):
                return
            if l[i] == None:
                return
            b = BinaryTreeNode(l[i])
            b.left = init(b.left, l, i * 2)
            b.right = init(b.right, l, i * 2 + 1)
            return b
        
        if l == None:
            self.top = None
        else:
            self.top = None
            l = [None] + l
            self.top = init(self.top, l, 1)

    def inorder(self, b):
        if b is not None:
            self.inorder(b.left)
            print b.data
            self.inorder(b.right)
   
    def preorder(self, b):
        if b is not None:
            print b.data
            self.preorder(b.left)
            self.preorder(b.right)
            
    def postorder(self, b):
        if b is not None:
            self.postorder(b.left)
            self.postorder(b.right)
            print b.data
    
    def leveloerder(self):
        l = []
        if self.top == None:
            return;
        l.insert(0, self.top)
        while True:
            if len(l) != 0:
                m = l.pop()
                print m.data
                if m.left != None:
                    l.insert(0, m.left)                    
                if m.right != None:
                    l.insert(0, m.right)                    
            else:
                break;

