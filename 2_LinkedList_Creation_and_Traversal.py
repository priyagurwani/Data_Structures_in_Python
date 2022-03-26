# Creation and traversing elements in LL using OOPS:
# Traversal : Visiting each element in a given LinkedList
class Node:
    def __init__(self,data):
        self.__data=data
        self.next=None
    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.head=None
    def print_elements(self):
        node=l1.head
        while (node!=None):
            print(node.get_data())
            node=node.next
n1=Node(10)   # n1 is an Object of class Node
n2=Node(20)   # n2 is an Object of class Node and so on 
n3=Node(30)
n4=Node(40)
n5=Node(50)

l1=LinkedList()  # l1 is an object of LinkedList class 
l1.head=n1      # Here, l1 object is connected to object of Node so it could traverse 
n1.next=n2      # the elements in given Linkedlist      
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=None
l1.print_elements()

