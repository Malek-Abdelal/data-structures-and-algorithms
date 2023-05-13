import re
class Node :
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    counter = 0
    def __init__(self, head = None):
        self.head = head


    def insert(self, value):
        if self.head == None:
            LinkedList.counter += 1
        LinkedList.counter += 1
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def to_string(self):
        current = self.head
        values = ""
        while current:
            values += f"{ {current.value} } -> "
            list_values = re.sub(r"\'", ' ', values)
            current = current.next 
        list_values += "NONE"
        return list_values
        
if __name__ == "__main__":
    f_node = Node(1)
    f_linked_list = LinkedList()
    # print(f_linked_list.head)
    print(LinkedList.counter)
    f_linked_list.insert(2)
    f_linked_list.insert(2)
    f_linked_list.insert(2)
    print(LinkedList.counter)
    print(f_linked_list.to_string())
    # print(f_linked_list.head)
    # print(f_node.value)