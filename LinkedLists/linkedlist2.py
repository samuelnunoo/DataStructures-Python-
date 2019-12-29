#Doubly Linked List
class DoublyLinkedList:
    #Init
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Node Object
    class Node:
        def __init__(self,data):
            self.data = data
            self.previous = None
            self.next = None

    #Iterators
    class Iterator:
        def __init__(self,head):
            self.trav = head

        def __iter__(self):
            return self

        def __next__(self):
            if self.trav  == None:
                raise StopIteration

            data = self.trav.data
            self.trav = self.trav.next
            return data




        def next(self):
            data = self.trav.data
            self.trav = self.trav.next
            return data
    def Iterate(self):
        trav = self.head
        while trav != None:
            data = trav.data
            yield data
            trav = trav.next


    # Insert Operations
    def insert(self, index, node):
        # Constraints:   1  ... size of list + 1
        if (index < 0 or index > self.size):
            raise Exception('Illegal Index')

        # Limits: 1 and size of list + 1 | prepend and append
        if (index == 0):
            self.addFirst(node)
            return True

        if (index == self.size ):
            self.addLast(node)
            return True

        # Set variables
        node = self.Node(node)
        trav = self.head

        # Traverse to the desired point
        for i in range(index):
            trav = trav.next


        #Set Node Values
        node.previous = trav.previous
        node.next = trav

        #Set List Values
        trav.previous.next = node
        trav.previous = node
    def addLast(self,elem):
        #Create the Node Objects
        node = self.Node(elem)


        #Check if Empty
        if self.isEmpty():
            #Set Node to Head and Tail
            self.head = node
            self.tail = node
        else:
            #Append node to Tail
            self.tail.next = node
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

        #Increase Size of List
        self.size += 1
    def addFirst(self,elem):

        #Check if Empty
        if self.isEmpty():

            #Set head and tail as same
            self.head = self.Node(elem)
            self.tail = self.head
        else:

            #Append new node to head
            self.head.previous = self.Node(elem)
            #Set the next of new node to preevious head
            self.head.previous.next = self.head
            #Define the new head as the new node
            self.head = self.head.previous

        #Increase size by One
        self.size += 1

    #Remove Operations
    def clear(self):

        #Set a variable to the Head Node
        trav = self.head

        #Begin a while loop that runs while trav is valid
        while trav!= None:

            #Set a variable for the next node
            next = trav.next

            #Remove Previous Next and Data of current Node
            trav.prev = None
            trav.next = None
            trav.data = None

            #Traverse to next Node
            trav = next


        #Reset Varibles
        self.head = None
        self.tail = None
        self.size = 0
    def removeFirst(self):

        #Check if list is Empty
        if self.isEmpty():
            raise Exception("Empty List")


        #Capture the data of the removed item
        data = self.head.data

        #Set the head to the next value and decrease size by one
        self.head = self.head.next
        self.size -= 1

        #Since you moved you don't know the current size so check if empty and set tail to none if it is
        if self.isEmpty():
            self.tail = None

        #Else set the previous of the head to None and return the data
        else:
            self.head.previous = None
        return data
    def removeLast(self):
        #Check if Empty
        if self.isEmpty():
            raise Exception("Empty List")

        #Set the Tail to the previous value and decrease size
        data = self.tail.data
        self.tail = self.tail.previous
        self.size -= 1

        #Check if Empty and set head to None if it is
        if self.isEmpty():
            self.head = None

        #Else clean up the removed value and return the captured data
        else:
            self.tail.next = None
        return data


    #Inspect Operations
    def isEmpty(self):
        return self.size == 0
    def listSize(self):
        return self.size
    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Empty List")
        return self.head.data
    def peekLast(self):
        if self.isEmpty():
            raise Exception("Empty List")
        return self.tail.data

































