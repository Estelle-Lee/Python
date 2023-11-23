#Queue with linked list node structure
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.num_nodes=0

    def size(self):
        return self.num_nodes
    
    def enqueue(self,value):
        new_node=Node(value)

        #if queue is empty
        if self.head is None:
            # self.head=new_node
            # self.tail=new_node
            self.head=self.tail=new_node    #same as above. multiple assignment
        else:   #if not empty
            # previous tail is now linked to the new node
            # and the new node is the new tail
            self.tail.next=new_node
            self.tail=new_node

        self.num_nodes+=1

    def dequeue(self):
        #the head contains the item that was added first
        #will begin by checking if the self.head attribute has a value of none
        #which means the queue is empty
        if self.head is None:
            return None
        
        #not returning the node but it's returning the node's value only
        dequeue_node_value=self.head.value

        #set the self.head attribute to self.head.next
        #set the next node in the queue to be the new head
        #by doing this, we have effectively removed the previous head from the queue
        self.head=self.head.next
        self.num_nodes-=1
        return dequeue_node_value
    

q=Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size()==3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size()==4) else "Fail")

print("Pass" if (q.dequeue()=='a') else "Fail")
print("Pass" if (q.dequeue()=='d') else "Fail") #print fail but que decrement count should increase because dequeue still decrement 'b'
print("Pass" if(q.size()==2) else "Fail")
