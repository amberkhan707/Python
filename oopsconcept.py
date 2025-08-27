# Inheritance + Polymorphism

# Parent Class
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal): #inheritance hua yha pe child of the animal parent
    def speak(self):  # polymorphism hua same method but different behavior from cat 
        return "Woof!"

class Cat(Animal):  
    def speak(self):    # polymorphism hua same method but different behavior from dog
        return "Meow!"
    def climb(self):
        return "quickly climb on tree"

# Objects
dog = Dog()
cat = Cat()

print(dog.speak())   # Woof!
print(cat.speak(),"     ",cat.climb())   # Meow!


# Encapsulation + Abstraction
class Human:
    def __init__(self,Name,Age): #Encapsulation - ek box ke ander data band h 
        self.name = Name  #public attribute
        self.__age = Age  #private attribute
    
    def get_age(self):
        return self.__age  #Abstraction - controlled accesss

Human1 = Human("Amber", "22")

print(Human1.name,Human1.get_age())
