class Node() :
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    # end of constructor

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else : #its a node having the insert method
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else: 
                    self.right.insert(value)
        else:
            self.value = value
    # end of insert
    
    def printTree(self):
        if self.right:
            self.right.printTree()
        if self.left:
            self.left.printTree()
        print(self.value)
    # end of printTree
# end of class Node

j = Node(5)
# j.insert()
j.insert(9)
j.insert(3)

j.printTree()


