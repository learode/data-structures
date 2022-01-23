class Queue():
    def __init__(self):
        self.container = []
        self.limit = 3
        self.head = 0
        self.tail = -1
    # end of constructor

    def is_empty(self):
        return len(self.container) == 0
    # end of is_empty

    def is_full(self):
        return len(self.container) >= self.limit
    # end of is_full

    def enqueue(self, ele):
        if self.is_full():
            output = 'Oh my! :D the queue is full.'
        else:
            self.container.append(ele)
            self.tail += 1
            output = 'Element successfully ended.'
        return output
    # end of enqueue

    def dequeue(self):
        if self.is_empty():
            output = 'Joe, :[ what do you want to remove, it\'s empty.'
        else:
            output = str(self.container.pop(self.head))
        return output
    # end of dequeue

    def peek(self):
        return self.container[self.head]
    # end of peek
# end of class Queue


h = Queue()

print(h.enqueue(5))
print(h.peek())
print(h.enqueue(34))
print(h.enqueue(67))
print(h.peek())
print(h.dequeue())
print(h.dequeue())
print(h.peek())