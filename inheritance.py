class Person():
    gender = "MALE"
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def greet():
        print("Welcome to the School")

    def print_name(self):
        print("hello",self.name)
    

class Student(Person):
    def __init__(self, branch, name):
        super().__init__(name)
        self.branch = branch
        super().print_name()
        print(super().gender) # class variable can we accessed via super() but not instance attributes
        

s1 = Student("Civil", "ASHU")
print(s1.branch)
s1.greet()

print(s1.name) # this line doesn't work before writing super() method
s1.print_name()