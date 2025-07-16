from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod 
    def speak(self): 
        pass 

    @abstractmethod 
    def move(self) :
        pass

    def sleep(slef): 
        print("Zzz.. Sleepling! ")

class Dog(Animal): 
    def speak(self):
        return "Woof!"
    
    def move(self): 
        return "Running on your legs"
    
class Bird(Animal): 
    def speak(self): 
        return "chirp"
    
    def move(self):
        return "Flying"
dog = Dog() 
print(dog.speak)
dog.sleep
