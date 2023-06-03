import re
import math

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
        list_values = ""
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

    
    def kth_from_end(self, k):
        current = self.head
        length = 0
        while current :
            length += 1
            current = current.next

        current = self.head

        try:
            if k < 0 :
                raise ValueError("Negative values are not allowed")
            while current :
                length -= 1
                if (k == length):
                    return current.value
                current = current.next
            current = self.head
            if self.head:
                return ("Your input exceed the length of the array, please inter a valid number !")
            return ("Your linked list is empty !")
        except ValueError:
            return('Negative values are not allowed !')


    def node_at_the_middle(self):
        current = self.head
        length = 0
        middle = 0
        while current :
            length += 1
            current = current.next

        current = self.head
        length /= 2
        while current :
            middle += 1
            if (middle == math.ceil(length)):
                return current.value
            current = current.next
        return ("Your linked list is empty !")
    
        
    @staticmethod
    def zip_lists(list1, list2):     #All about pass by reference !!
        current1 = list1.head
        current2 = list2.head
        if current1 is None:
            return list2
        if current2 is None:
            return list1
        while current1 and current2:
            next1 = current1.next
            next2 = current2.next
            current1.next = current2
            current2.next = next1 or next2
            current1 = next1
            current2 = next2
        return list1.to_string()
       

    def check_palindrome(self, list):
        current = list.head
        values = []
        result = True
        while current :
            values.append(current.value)
            current = current.next
        x, y = 0,-1
        for i in range(len(values)//2):
            if values[x] == values[y]:
                result = True
            else : 
                result = False
                return result
            x+=1
            y-=1
        return result








if __name__ == "__main__":
    f_node = Node(1)
    f_linked_list = LinkedList(f_node)
    f_linked_list.append(3)
    f_linked_list.append(5)
    # f_linked_list.append(5)
    # f_linked_list.append(3)
    # f_linked_list.append(2)
    s_linked_list = LinkedList()
    s_linked_list.append(2)
    s_linked_list.append(4)
    s_linked_list.append(6)
    # f_linked_list.insert_before(2, 7)
    # f_linked_list.insert_after(1, 8)
    # f_linked_list.delete(7)
    # print(f_linked_list.check_palindrome(f_linked_list))
    # print(f_linked_list.to_string())
    print(s_linked_list.to_string())
    # print(s_linked_list.to_string())
    # print(f_linked_list.kth_from_end(0))
    # print(LinkedList.zip_lists(f_linked_list,s_linked_list))
    # print(f_linked_list.node_at_the_middle())

