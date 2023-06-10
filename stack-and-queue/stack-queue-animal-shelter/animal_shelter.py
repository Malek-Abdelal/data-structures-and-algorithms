class Animal:
    def __init__(self, kind, name, next = None):
        self.kind = kind
        self.name = name
        self.next = next


class AnimalShelter:
    def __init__(self, back = None, front = None):
        self.back = back
        self.front = front
        
    def __str__(self):
        current = self.front
        queue = ""
        while current:
            queue = f" <- {current.name}" + queue
            current = current.next
        return "None" + queue

    def enqueue(self, animal):
        if not self.back :
            self.back = animal
            self.front = animal
        else:
            self.back.next = animal
            self.back = animal

    def dequeue(self, pref):
        if not self.front:
            raise Exception("The queue is empty !")
        if pref != "cat" and pref != "dog":
            return None
        temp = self.front
        if self.front.kind == pref: 
            self.front = temp.next
            temp.next = None
            return temp.kind
        
        else:
            counter = 0
            found = False
            dequeued_value = None                         # ???
            while temp:
                counter += 1
                temp = temp.next
            temp = self.front

            for _ in range(counter - 1):
                if self.front.kind == pref and not found:
                    dequeued_value = self.front.name            # ???
                    self.front = temp.next
                    temp.next = None
                    temp = self.front
                    found = True
                  
                self.front = temp.next
                temp.next = None
                self.enqueue(temp)
                temp = self.front
            counter += 1



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
print(shelter)           # Output =>  None <- joyyy <- locyyy <- joyy <- locyy <- joy <- locy
shelter.dequeue("dog")
print(shelter)           # Output =>  None <- joyyy <- locyyy <- joyy <- locyy <- locy