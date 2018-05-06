class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        del(self.items[0])
        return self.items

    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)

q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
q.display()

print(q.items)

q.dequeue()
q.display()