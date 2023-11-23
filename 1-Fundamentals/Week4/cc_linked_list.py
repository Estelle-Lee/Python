class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        # pointing 
        self.head=None

    def append(self,value):
        new_node=Node(value)

        # doesn't have a node?
        if self.head is None:
            self.head=new_node
            print("Head Node created:",self.head.value)
            return
        
        # already has a head?
        # now define tail
        node=self.head
        while node.next is not None:
            node=node.next

        node.next=new_node
        print("Append new Node with value:",node.next.value)

    def prepend(self,value):
        # instantiate a new object of the Node class, using the value passed in.
        prepend1=Node(value)
        
        #if the self object does not have a head attribute,
        if self.head is None:
            #assign the new node object you just instantiated as the head,
            self.head=prepend1
            #and print the message "head node created" followed by the value of the node
            print(f"Head Node created: {self.head.value}")
        else:
            #if the self object already has a head node, 
            #you will then write code to assign the new node object as the new head
            #the exisitng head must be linked to the new head
            prepend1.next=self.head
            self.head=prepend1
            print(f"Prepended new Head Node with value: {self.head.value}")
            
            if self.head.next:
                print(f"Node following Head is: {self.head.next.value}")



llist=LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")