class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.number  = 5

# Now we know Student and Professor both are Wizard
# Let's try to use Wizaed funtionality inside them

class Student(Wizard):
    def __init__(self, name, house): # initialization of object
        super().__init__(name)
        # Even though Student inherits from Wizard, the child class (Student) is responsible 
        # for calling the parent’s constructor (__init__) and providing the required arguments (name in this case).
        self.name = name
        self.house = house 

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)  # calls Wizard.__init__
        self.subject = subject


student = Student("Harry", "Patna")
professor = Professor("Nirmal", "mumbai")

print(student.name)
print(student.number)
print(professor.name)


# Example for inherting multiple class inside one class
'''
class A:
    def __init__(self, a_value):
        print("A's __init__ called with:", a_value)

class B:
    def __init__(self, b_value):
        print("B's __init__ called with:", b_value)

class C(A, B):
    def __init__(self, a_value, b_value):
        print("C's __init__ called")
        A.__init__(self, a_value)  # manually call A's init
        B.__init__(self, b_value)  # manually call B's init

obj = C("Value for A", "Value for B")
'''