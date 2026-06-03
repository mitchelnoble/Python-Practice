#class based model in python, clearly defined syntax for attributes and methods
#Object Oriented Programming boiled down is defining classes, creating instances of those classes, and implementing inheritance to extend or modify the behavior of the instances of those classes.

class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    return f"{self.name} makes a sound."
  
class Dog(Animal):
  def speak(self):
    return f"{self.name} barks."
  
# Using the classes
generic_animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(generic_animal.speak()) #Output: Generic Animal makes a sound.
print(dog.speak()) #Output: Buddy barks

#the Dog class inherits the animal class's function "speak" and modifies it. If dog.speak is used it "barks" and if generic_animal.speak is used it "makes a sound"