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
                # attaching the remaining nodes after our prev_value to the new node, so that they don't get missed
                new_node.next = curr.next
                # now assigning the next of current node to new_node, it will break connection between current node 
                # and all nodes after that, But we've already assigned the remaining nodes to new node
                curr.next = new_node
                self.n +=1 
                break
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

    def delete_head(self):
        if self.head != None:
            self.head = self.head.next
            self.n -=1
            return self.head
        else:
            return "No node to delete"
        
    def pop(self):
        curr = self.head
        if curr == None:
            return "Empty linked list"
        if curr.next == None:
            return self.delete_head()
    
        # Use this condition very carefully, as only using this won't work when linkedlist has single item
        while(curr.next.next != None):
            curr = curr.next
        curr.next = None    
        self.n -=1
        return self.head
    
    def delete_specific_node(self, value):
        curr = self.head
        if curr == None:
            return "Linked list is empty"
        
        if curr.data == value:
            self.head = self.head.next
            return self.head
        prev = curr
        while curr.next != None:
            if curr.next.data == value:
                print(" pehle ", curr.data)
                curr.next = curr.next.next
                print("baad me", curr.data)
                break
            # prev = curr    
            curr = curr.next    

        # while curr != None:
        #     if curr.data == value:
        #         print(" pehle ", prev.data)
        #         prev.next = curr.next
        #         print("baad me", prev.data)
        #         break
        #     prev = curr    
        #     curr = curr.next    



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
print(l1.len())
l1.traverse()

l1.delete_specific_node(3)
l1.traverse()

l1.delete_specific_node(5)
l1.traverse()

l1.delete_specific_node(9)
l1.traverse()

l1.delete_specific_node(1)
l1.traverse()

l1.delete_specific_node(10)
l1.traverse()
# print(l1.search())

# a = Node(1)     
# b = Node(2)  
# a._next = b 
# print(a._data)
# print(id(a._next))
# print(id(b))