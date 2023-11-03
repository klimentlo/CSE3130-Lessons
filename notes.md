// notes.md
# Object Oriented Programming 2 - Notes
## Inheritance
Inheritance is the process where one class inherits attributes and methods from another class. While some languages, such as java restrict it, classes can inherit from multiple parent classes.
* multiple parent classes are often avoided because there are potential conflicts when both parent classes have the same attribute or method names

### Identifying when to use Inheritance
Inheritance describes an _Is-A_ relationship
* The _deck_ __is_a__ _group of cards_ and the _hand_ __is a__ _group of cards_, but the _deck_ is NOT a _hand_. Therefore, a _deck_ and _hand_ can both inherit from a _group of cards_, but they are not related to each other.
* If the object fits into the sentence, "the (object 1) is a (object 2)," then object 1 can be a sub-class of object 2
* Inheritance often reveals itself during the design process, when multiple classes have similar attributes and methods
* __Abstract Classes__ (as opposed to concrete classes) are classes that are never instantiated by themselves. These classes are made solely for the purpose of inheritance. Oftentimes these classes have abstract methods which can not fully function within the abstract class; instead, they rely on data in their respective classes
* Example: MySprite class does not have a Surface object in self.__Surface

Note: When making uml tables, make sure the child uml table has arrows pointing into the parent uml table that they're inheriting attributes from. Child --> Parent
```python
class Mammal: # Abstract Parent Class
    def __init__(self, genus, species, name):
        self.genus = genus
        self.species = species
        self.name = name
        self.crySound = None

    def setCry(self, sound):
        self.crySound = sound
        
    def getCry(self):
        return self.crySound
    
class Dog(Mammal): # concrete child class
    def __init__(self, genus, species, name="Rover"):
        Mammal.__init__(self, genus, species, name)
        self.setCry("Bark")
        # add additional attributes
    
    # add additional methods
    
class Cat(Mammal): # concrete child class
    def __init__(self, name):
        Mammal.__init__(self, "Felis", "Catis", name)
        self.setCry("Meow")

HUSKY = Dog("Canis", "Cupis", "Husky")
SIAMESE = Cat("Cocoa")
```

## Polymorphism
Polymorphism is the ability to have the same method is different subclasses perform different tasks/different outcomes. In some cases, the parent class will have the method that is close but not perfectly aligned to the needs of a child class. The child class can then call on the parent class and modify it. 
* Example includes modifying the __init__(self) class of the parent class. 
* Example includes the WASDmove() of ImageSprites, which still uses the WASDmove() of the parent class, but add on the image flip when moving.
