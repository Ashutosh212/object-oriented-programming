from abc import ABC, abstractmethod
# abstract base class(abc)

class Animal(ABC):
    def __init__(self):
        self.legs = 4

    @abstractmethod
    def make_sound():
        pass

class Dog(Animal):
    species = "Canine"  # ✅ class variable

    def __init__(self, name):
        self.name = name

    def make_sound(): # you must compulsory have to create this
        pass

    @classmethod
    def make_from_string(cls, name_str):
        # cls refers to the class, so this works even in subclasses
        return cls(name_str)

    @classmethod
    def wooh_species(cls):
        return f"{cls.species * 3}"
    
    @staticmethod
    def bark(times):
        return "Woof! " * times
    
    def access_classmethods(self):
        # return self.wooh_species()  #both will work
        return Dog.wooh_species()

    def custom_bark(self, n):
        # return self.bark(n)
        return Dog.bark(n)   # using staticmethod with Class level reference


# animal = Animal() # Can't instantiate abstract class Animal 
dog = Dog.make_from_string("Bruno")
print(dog.name)        # Bruno
print(dog.species)     # Canine
print(dog.custom_bark(3))     # Woof! Woof! Woof!
print(dog.access_classmethods())