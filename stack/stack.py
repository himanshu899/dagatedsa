# LIFO - Last in first out
# |_______|
# |_______|
# |_______|
# |_______|

# If you want to implement stack using a linked list -> all operations are to be performed using head of the linked list.
# Insertion on head will make the most recent or the last in element at the head ... and pop will remove the most recent if we operate from head
# 
class Node:
    def __init__ (self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        # It will have a top element as stack only knows the most recent element .... None implies empty stack
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, value):
        # adding element to head of the linked list
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top       
            self.top = new_node
        return self.top
        
    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        
        top_node = self.top
        self.top = self.top.next
        return top_node.data
    
    def traverse(self):
        temp = self.top
        while temp != None:  
            print(temp.data, end=" ")   
            temp = temp.next
        print()

s1 = Stack()
s1.push(9) 
s1.push(8) 
s1.push(7) 
s1.push(6) 
s1.push(5)         
s1.push(3) 
s1.push(91)
s1.traverse()
print(s1.pop())
s1.traverse()
