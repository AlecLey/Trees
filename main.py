class B_Tree:

    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None


    def insertLeft(self, new_node):
        if self.leftChild == None:
            self.leftChild = B_Tree(new_node)
        else:
            t = B_Tree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t


    def insertRight(self, new_node):
        if self.rightChild == None:
            self.rightChild = B_Tree(new_node)
        else:
            t = B_Tree(new_node)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild


    def getLeftChild(self):
        return self.leftChild


    def setRootVal(self, obj):
        self.key = obj


    def getRootVal(self):
        return self.key

def tree_size(t):
    if t != None:
        size = 1
        if t.getRightChild() != None:
            size= size + 1
            t.getRightChild()
            t.getLeftChild()
        else:
            size += 0

def preorder(tree):
    if tree != None:
        print(tree.getRootVal(), end = " ")
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), end = " ")


def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal(), end = " ")
        inorder(tree.getRightChild())


def main():
    print('''
        Creating the tree:

                 a
                / \\
               b   c
              / \\   \\
             d   e   f
                /
               g

    ''')
    t = B_Tree('a')
    t.insertLeft('b')
    t.insertRight('c')
    t.getLeftChild().insertRight('e')
    t.getLeftChild().insertLeft('d')
    t.getLeftChild().getRightChild().insertLeft('g')
    t.getRightChild().insertRight('f')

    print("Inorder traversal:")
    inorder(t)

    print("\n\nPreorder traversal:")
    preorder(t)

    print("\n\nPostorder traversal:")
    postorder(t)

    print(tree_size)


if __name__ == "__main__":
    main()




