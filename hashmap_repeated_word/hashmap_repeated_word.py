import re

class Node:
    """
    Represents a node in a linked list or other data structure.
    
    Attributes:
        value: The value contained in the node.
        next: A reference to the next node.
    """
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    """
    Represents a singly linked list data structure.
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the beginning of the linked list.
        
        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class HashTable:
    """
    Stores key-value pairs of data using buckets to improve data access efficiency.
    """
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.keys = []

    def __hash(self, key):
        """
        Returns the hash code of the given key.
        
        Args:
            key: The key for which the hash code needs to be calculated.
        
        Returns:
            The hash code (index) for the key.
        """
        return sum([ord(str(char)) for char in key]) * 283 % self.__size
    
    def set(self, key, value):
        """
        Sets a key-value pair in the bucket, handling collisions as needed.
        
        Args:
            key: The key to be hashed and used as the identifier for the value.
            value: The value associated with the key.
        """
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll

        self.__buckets[index].insert([key, value])
        self.keys.append(key)

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hashtable.
        
        Args:
            key: The key for which the value needs to be retrieved.
            
        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        return None

    def has(self, key):
        """
        Checks if the given key exists in the hashtable.
        
        Args:
            key: The key to check for existence.
            
        Returns:
            True if the key exists, False otherwise.
        """
        if self.get(key):
            return True
        return False

    def all_keys(self):
        """
        Returns a list of all the keys present in the Hashtable.
        """
        return self.keys.copy()

def find_first_repeated_word(input_string):
    """
    Finds the first repeated word in a given string.
    
    Args:
        input_string: The input string in which to search for the repeated word.
        
    Returns:
        The first repeated word found, or "No Repetition" if no repetition is found.
    """
    hashtable = HashTable()
    temp = ""
    word = ""
    pattern = r"[^\w\s]"
    cleaned_string = re.sub(pattern, "", input_string)

    for i in range(len(cleaned_string) - 1, -1, -1):
        if cleaned_string[i] != ' ':
            temp += cleaned_string[i]
        else:
            if hashtable.has(temp):
                word = temp
            else:
                hashtable.set(temp, 1)
            temp = ""

    if hashtable.has(temp):
        word = temp

    if word != "":
        word = word[::-1]
        return word
    else:
        return "No Repetition"
