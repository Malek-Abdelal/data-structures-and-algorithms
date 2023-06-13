from stack.stack import Stack

class PseudoQueue:
    def __init__(self):
        """
        Initializes a new instance of the PseudoQueue class.
        It creates two empty stacks to simulate a queue.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = self.stack1.top

    def __str__(self):
        """
        Returns a string representation of the PseudoQueue.
        It traverses stack1 and returns the elements in a string format.
        """
        current = self.stack1.top
        stack = ""
        while current:
            stack += f"{current.value} -> "
            current = current.next
        return stack + "None"

    def enqueue(self, value):
        """
        Adds a value to the rear of the PseudoQueue (simulated queue).

        Args:
            value: The value to be added to the PseudoQueue.
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        Removes and returns the value at the front of the PseudoQueue (simulated queue).

        Returns:
            The value at the front of the PseudoQueue.

        Raises:
            Exception: If the PseudoQueue is empty.
        """
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
