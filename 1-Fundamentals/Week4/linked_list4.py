#Doubly linked list

class DoubleNode:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        new_node=DoubleNode(value)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
            print("Head Node created:",self.head.value)
            return
        
        #finding tail node don't need while loop
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
        print("Append new Node with value:",self.tail.value)

dllist=DoublyLinkedList()
dllist.append("First Node")

'''
$ python -i linked_list4.py
Head Node created: First Node
>>> dllist.head.value
'First Node'
>>> dllist.tail.value
'First Node'
>>> dllist.append("Second Node")
Append new Node with value: Second Node
>>> dllist.head.value
'First Node'
>>> dllist.tail.value
'Second Node'
>>> dllist.head.next.value
'Second Node'
>>> dllist.tail.prev.value
'First Node'
>>> dllist.append("3rd")
Append new Node with value: 3rd
>>> dllist.tail.value
'3rd'
>>> dllist.head.prev.value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'      
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'value'
>>> dllist.tail.prev.prev.value
'First Node'
>>> dllist.head.next.next.value
'3rd'
>>> exit()
'''