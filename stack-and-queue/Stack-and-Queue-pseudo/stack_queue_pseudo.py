from stack.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        current = self.stack1.top
        stack = ""
        while current:
            stack += f"{current.value} -> "
            current = current.next
        return stack + "None"

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if not self.stack1.top:
            raise Exception("The stack is empty !")
        
        current = self.stack1.top
        while current:
            current = current.next
            self.stack2.push(self.stack1.pop())
        popped_value = self.stack2.pop()
        current = self.stack2.top
        while current:
            current = current.next
            self.stack1.push(self.stack2.pop())
        return popped_value
    

new_queue = PseudoQueue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print(new_queue)
print(new_queue.dequeue())
print(new_queue)
