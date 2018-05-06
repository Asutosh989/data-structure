class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop_(self):
        # if(not isEmpty()):
        del(self.items[len(self.items) - 1])
        return self.items
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)

s = Stack()
s.display()
s.push(2)
s.push(9)
s.push(10)
s.push(4)
s.display()
print(s.size())
s.pop_()
s.display()
