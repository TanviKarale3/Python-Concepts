#In this program, we define a base class called Animal with an abstract method called make_sound.
# We also define three subclasses, Dog, Cat, and Cow, each of which overrides 
#the make_sound method with its own implementation.


class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Cow(Animal):
    def make_sound(self):
        return "Moo!"
    
def animal_sounds(animal):
    print(animal.make_sound())
    
dog = Dog("Fido")
cat = Cat("Fluffy")
cow = Cow("Bessie")

animal_sounds(dog)   # Output: "Woof!"
animal_sounds(cat)   # Output: "Meow!"
animal_sounds(cow)   # Output: "Moo!"