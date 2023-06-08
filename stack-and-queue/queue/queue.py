from node.node import Node

class Queue:
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def __str__(self):
        current = self.front
        queue = ""
        while current:
            queue = f" <- {current.value}" + queue
            current = current.next
        return "None" + queue

    def enqueue(self, value):
        new_node = Node(value)
        if not self.back :
            self.back = new_node
            self.front = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        try:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        except AttributeError:
            return "The queue is empty !"

    def peek(self):
        try:
            if self.front == None:
                raise EmptyQueueError
            return self.front.value
        except EmptyQueueError:
            return "The queue is empty !"

    def is_empty(self):
        return self.front == None


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__("The queue is empty !")



# def DuckDuckGoose(list, k):
#     queue = Queue()
#     # queue2 = Queue()
#     for ele in list:
#         queue.enqueue(ele)
    

#     for i in range(4):
#         current = queue.front
#         counter = 0     
#         while current:
#             counter += 1
#             if counter == k:
#                 queue.dequeue()
#             queue.enqueue(queue.dequeue())
#             if current.value == queue.front.value and counter != 0 :
#                 break
#         print(queue)
#         # current = current.next
        


    # current = queue.front
    # temp = None
    # for i in range(k-1):
    #     queue2.enqueue(queue.dequeue())
    #     # current = current.next or queue.front
    # queue.dequeue()
    # while current:
    #     queue2.enqueue(queue.dequeue())
    #     current = current.next
    # queue2.enqueue(queue.dequeue())


    # print("original", queue)

# list1 = ["a","b","c","d","e"]
# k = 3
# DuckDuckGoose(list1, k)


    # while current.next:



    



queue1 = Queue()
# queue1.enqueue(1)
# queue1.enqueue(2)
# queue1.enqueue(3)
# queue1.dequeue()
# queue1.dequeue()
# queue1.dequeue()
# print(queue1)
# # print(queue1.dequeue())
# print(queue1)
# print(queue1.peek())
# print(queue1.is_empty())
# print(queue1.front.value)
# print(queue1.back.value)