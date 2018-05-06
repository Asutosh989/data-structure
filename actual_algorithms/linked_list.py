class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        # create a new node for the data
        new_node = Node(data)
        # pont the new node to the current head
        new_node.next = self.head
        # assign the new node as the head
        self.head = new_node
    
    def insert_after(self, previous_position, data):

        # check if the previous node exist
        if previous_position is None:
            print("The previous node is not in the linked list")
            return
        
        new_node = Node(data)
        # assign the next of previous to new node
        new_node.next = previous_position.next
        # assign the next of previous node to new node
        previous_position.next = new_node

    def insert_last(self, data):
        new_node = Node(data)

        # Check if linked list exist. If not, assign the newnode as head
        if self.head is None:
            self.head = new_node
            return

        # else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        
        # now last is the last node of Linked list
        # assigning next of last to new node
        last.next = new_node
        # next of new node is None by default as mentioned by the attributes of the Node object

    def printList(self):
        node = self.head
        d = []
        while(node.next):
            d.append(str(node.val))
            node = node.next
        print(' '.join(d))

if __name__ == '__main__':
    l = Linked_List()
    l.insert_last(3)
    l.printList()
    l.insert_last(8)
    l.printList()
    # l.insert_last(78)
    # l.printList()
    l.insert_at_front(1)
    l.printList()
    l.insert_at_front(10)
    l.printList()
    l.insert_after(l.head.next, 15)
    l.printList()
    l.insert_after(l.head.next.next, 20)
    l.printList()
    l.insert_last(30)
    l.printList()
    print(l.head.val)
