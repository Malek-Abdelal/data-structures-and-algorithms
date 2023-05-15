import re
class Node :
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head = None):
        self.head = head


    def insert(self, value):
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
    

    def append(self, value):
        current = self.head
        if self.head is None:
            self.head = Node(value)
        else: 
            while current:
                if current.next is None:
                    current.next = Node(value)
                    break
                current = current.next


    def insert_before(self, value, new_value):
        current = self.head
        new_node = Node(new_value)
        if current.value == value:    
            new_node.next = self.head
            self.head = new_node
        else: 
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
        

    def insert_after(self, value, new_value):
        current = self.head
        new_node = Node(new_value)
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    
    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next



if __name__ == "__main__":
    f_node = Node(1)
    f_linked_list = LinkedList()
    f_linked_list.insert(2)
    f_linked_list.insert(1)
    f_linked_list.append(5)
    f_linked_list.insert_before(2, 7)
    f_linked_list.insert_after(1, 8)
    f_linked_list.delete(7)
    print(f_linked_list.to_string())

