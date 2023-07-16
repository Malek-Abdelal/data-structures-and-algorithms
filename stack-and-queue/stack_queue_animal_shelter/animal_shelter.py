class Animal:
    def __init__(self, kind, name, next = None):
        """
            Initializes an instance of the Animal class.

            Args:
                kind (str): The type or kind of the animal.
                name (str): The name of the animal.
                next (Animal, optional): The reference to the next animal in the queue. Defaults to None.
        """
        self.kind = kind
        self.name = name
        self.next = next


class AnimalShelter:
    def __init__(self, back = None, front = None):
        """
        Initializes an instance of the AnimalShelter class.

        Args:
            back (Animal, optional): The reference to the back of the queue. Defaults to None.
            front (Animal, optional): The reference to the front of the queue. Defaults to None.
        """
        self.back = back
        self.front = front
        
    def __str__(self):
        """
        Returns a string representation of the animal queue.

        Returns:
            str: A string representation of the animal queue.
        """
        current = self.front
        queue = ""
        while current:
            queue = f" <- {current.name}" + queue
            current = current.next
        return "None" + queue

    def enqueue(self, animal):
        """
        Enqueues an animal into the shelter queue.

        Args:
            animal (Animal): The animal object to be enqueued.
        """
        if not self.back :
            self.back = animal
            self.front = animal
        else:
            self.back.next = animal
            self.back = animal

    def dequeue(self, pref):
        """
        Dequeues an animal from the shelter queue based on the preference.

        Args:
            pref (str): The preference for the type of animal to dequeue ("cat", "dog", or any other value).

        Returns:
            str: The name of the dequeued animal.

        Raises:
            Exception: If the queue is empty.
        """
        if not self.front:
            raise Exception("The queue is empty !")
        temp = self.front
        if (self.front.kind == pref) or (pref != "cat" and pref != "dog"): 
            self.front = temp.next
            temp.next = None
            return temp.name
        
        else:
            counter = 0
            found = False
            dequeued_value = None                     
            while temp:
                counter += 1
                temp = temp.next
            temp = self.front

            for _ in range(counter - 1):
                if self.front.kind == pref and not found:
                    dequeued_value = self.front.name           
                    self.front = temp.next
                    temp.next = None
                    temp = self.front
                    found = True
                  
                self.front = temp.next
                temp.next = None
                self.enqueue(temp)
                temp = self.front
            counter += 1
            return dequeued_value



animal1 = Animal("cat", "locy")
animal2 = Animal("dog", "joy")
animal3 = Animal("cat", "locyy")
animal4 = Animal("dog", "joyy")
animal5 = Animal("cat", "locyyy")
animal6 = Animal("deg", "joyyy")
shelter = AnimalShelter()
shelter.enqueue(animal1)
shelter.enqueue(animal2)
shelter.enqueue(animal3)
shelter.enqueue(animal4)
shelter.enqueue(animal5)
shelter.enqueue(animal6)
print(shelter)                  # Output =>  None <- joyyy <- locyyy <- joyy <- locyy <- joy <- locy
print(shelter.dequeue("lion"))  # Output => joy
print(shelter)                  # Output =>  None <- joyyy <- locyyy <- joyy <- locyy <- locy