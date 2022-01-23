class Stack():
    def __init__(self):
        self.container = []
        self.limit = 3
        self.top = -1 # last ele of array
        # self.type = self.what_type()
    # end of constructor

    def is_full(self):
        return len(self.container) >= self.limit
    # end of is_full
    def is_empty(self):
        return (len(self.container) == 0)
    # end of is_empty


    def push(self, ele):
        if self.is_full():
            return 'ERROR! LIMITS REACHED. :('
        else:
            self.container.append(ele)
            self.top += 1
        return 'Successfully pushed.'
    # end of push

    def pop(self):
        if self.is_empty():
            return 'Ohs! :O stack is empty.'
        else:
            poped = self.container.pop(self.top)
            self.top -= 1
            return str(poped)
    # end of pop
    
    def peek(self):
        if self.top == -1:
            return str(self.container)
        return str(self.container[self.top])
    # end of peek
# end of class Stack

aStack = Stack()

print(aStack.push(54))
print(aStack.push('23'))
print(aStack.peek())

print(aStack.push(342))
print(aStack.push(54))
print(aStack.push(67))
print(aStack.pop())
print(aStack.peek())

print(aStack.pop())
print(aStack.pop())
print(aStack.pop())
print(aStack.pop())
print(aStack.peek())
