class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
        # n is no. of nodes in the linked list
        self.n = 0

    def insert_head(self, value):
        # insertion at the begining of the ll
        # creating new node with data as value
        new_node = Node(value)
        # create connection, now new_node has the address of the head and head itself has the address of the next node
        new_node.next = self.head
        # reassign head
        self.head = new_node
        self.n += 1
        return new_node

    def insert_tail(self, value):  
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1 
            return new_node
        
        curr = self.head
        # checking till the last node ... curr.next = None implies it is the last node
        while(curr.next != None):
            curr = curr.next
        # we're at the last node, inserting the data to the next of the last node
        curr.next = new_node
        self.n +=1
        return new_node
    
    def insert_after(self, prev_value, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return new_node
        
        curr = self.head
        while(curr != None):
            if curr.data == prev_value:
                new_node.next = curr.next
                # temp = curr.next
                curr.next = new_node
            curr = curr.next
        return new_node
    
    def insert(self, data):
        temp = self.head
        prev = self.head
        while(temp != None):
            prev = temp
            temp = temp.next

        prev.next = data

    def traverse(self):
        curr = self.head
        result = ''
        while(curr != None):
            result = result + str(curr.data) + '->'
            curr = curr.next

        print(result[:-2])    

    def search(self):
        return

    def delete(self):
        pass

    def len(self):
        return self.n

l1 = LinkedList()
l1.insert_tail(10)
l1.insert_head(1)
l1.insert_head(2)
l1.insert_head(3)
l1.insert_head(5)
l1.insert_tail(9)
l1.insert_after(1, 8)

# print(l1.head.data)
# print(l1.len())
l1.traverse()
# print(l1.search())

# a = Node(1)     
# b = Node(2)  
# a._next = b 
# print(a._data)
# print(id(a._next))
# print(id(b))