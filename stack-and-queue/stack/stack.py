from node.node import Node

class Stack:
    def __init__(self, top = None):
        self.top = top

    def __str__(self):
        current= self.top
        stack = ""
        while current:
            stack += f"{current.value} -> "
            current = current.next
        return stack + "None"

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        try :    
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp.value
        except AttributeError:
            return "The stack is empty !"

    def peek(self):
        try:
            if self.top == None:
                raise EmptyStackError
            return self.top.value
        except EmptyStackError:
            return "The stack is empty !"
    
    def is_empty(self):
        return self.top == None
    

class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("The stack is empty !")

stack1 = Stack()
stack1.push(1)
stack1.push(2)
# stack1.pop()
# print(stack1.peek())
# print(stack1.is_empty())
# print(stack1.top.next.value)
print(stack1)

