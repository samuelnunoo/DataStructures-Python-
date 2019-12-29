from LinkedLists.linkedlist2 import DoublyLinkedList as LinkedList


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self,node):
        self.list.append(node)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        return self.list.remove

    def size(self):
        return self.list.psize()

    def isEmpty(self):
        return self.size() == 0


stack = Stack()

stack.push(3)
stack.pop()
print(stack.size())
