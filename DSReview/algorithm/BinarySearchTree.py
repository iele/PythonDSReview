import algorithm.BinaryTree

class BinarySearchTree(algorithm.BinaryTree.BinaryTree):
    def __init__(self, l=None):
        self.top = None
        if l is not None:
            for i in l:
                self.insert(i)
   
    def search(self, data):
        n = self.top
        while n != None:
            if data == n.data:
                return n
            elif data < n.data:
                n = n.left
            elif data > n.data:
                n = n.right
        return None               
      
    def __modsearch(self, data):
        n = self.top
        on = self.top
        while n != None:
            if data == n.data:
                return None
            elif data < n.data:
                on = n
                n = n.left
            elif data > n.data:
                on = n
                n = n.right
        return on          

    def insert(self, data):
        t = self.__modsearch(data)
        if t != None and self.top != None:
            p = algorithm.BinaryTree.BinaryTreeNode(data)
            if t.left > data:
                t.left = p
            else:
                t.right = p
        else:
            self.top = algorithm.BinaryTree.BinaryTreeNode(data)            
