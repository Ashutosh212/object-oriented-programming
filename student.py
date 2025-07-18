import sys
class Student:
    def __init__(self, name, house, patronus): # initialization of object

        self.name = name
        self.house = house  # this also going to call setter method
        self.patronus = patronus

        # print(self) # it's a location/memory
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
     
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter   #this will check if house attribute of object instances at both at creation and mutation
    def house(self, house):
        if house not in ["patna", "mumbai"]:
            raise ValueError("Invalid house")
        self._house = house 
        # We store the value somewhere else 
        # This line self.house = house calls the setter again, and again, and again.
        #  Python crashes with a RecursionError.
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "😇"
            case "Otter":
                return "😉"
            case _:
                return "😶‍🌫"
            
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)

def main():
    # student = get_student()
    student = Student.get()
    print(student) # refers to a location in ram/memory if you not initialise __str__
    # student.house = "delhi"  # calling setter, will give Error
    # NOTE:"student.house =" this thing first see any setter defined for this attribute or not before assiging any value to it blindly
    print("Expecto Patronum!")
    print(student.charm())


# def get_student(): # Migrating this function inside class only
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus) # constructor call
    
if __name__ == "__main__":
    main()
