class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head 
        while last.next:
            last = last.next 
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end= " -> ")
            temp = temp.next 
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.print_list() 
