## Four Pillars of OOPs

### Abstraction
Hiding the implementation details of a class and only showing the essential features to the users.

### Encapsulation
- **Encapsulation** is the practice of **hiding internal state and requiring all interaction to be performed through an object’s methods**. It helps protect the data from unintended access or modification.
- Wrapping data and function into single unit(object). 
- Think as: Bundling data and the methods that operate on that data into a single unit (class), and hiding the internal details from outside access.

### Inheritance
When one class derives(child) the properties & methods of another class(parent/base).

#### Single Inheritance 
#### Multi-level Inheritance 
#### Multiple Inheritance 
#### Super method
- super() method is used to access methods of the parent class.
- `super()` does **not give you direct access to instance attributes**. It is used to **call methods of the parent class**, not access its attributes directly.
- 
### Polymorphism: Operator Overloading

**Operator overloading** lets you redefine the behavior of built-in operators (`+`, `-`, `*`, etc.) for your custom classes.
Example = \_\_add\_\_

### Private attribute in python
- Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
- In Python, you can make them private by using __ in front of variable name but they are not actually private.
Instead of exposing the variable directly, use **methods** to control access.
```
class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        """Getter: Safe read-only access"""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """Setter: Safe write access with validation"""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
```

| Feature     | Benefit                                                            |
| ----------- | ------------------------------------------------------------------ |
| `@property` | You can **read it like an attribute**, but it's actually a method. |
| Validation  | You can **control what values get assigned**.                      |

### Dynamic Attribute Assignment in Python Classes
#### Scenario:
You define a class without specifying any attributes:

```
class Student:
	pass
```

Then you create an instance and assign a new attribute:
```

s = Student() 
s.rollnumber = 5 
print(s.rollnumber)  
# Output: 5`
```


Python classes allow **dynamic attribute assignment**. When you write:

You're dynamically adding a new attribute `rollnumber` to that **specific object `s`**, even though `rollnumber` was not defined inside the class.

You can see this using:

`print(s.__dict__) # Output: {'rollnumber': 5}`

Each object stores its attributes in a built-in dictionary called `__dict__`.


- ✅ In Python, calling a class like a function (e.g. `Student("Alice")`) creates an object.
- ⚙️ This triggers the `__init__()` method for object initialisation.
- ❌ A class is not literally a function, but can be **used like one** to create instances.

### Dunder

Dunder is short for "Double UNDERscore" — it refers to names in Python that start and end with two underscores, like:

##### What Dunder Methods Do

Dunder methods (also called magic methods or special methods) let you customize the behavior of your classes, especially how they behave with built-in operators and functions.


`self` give you access of the current object that created.
\_\_str\_\_ -> print the object information instead of memory location


### What is `@property`?

- `@property` is a **special decorator** in Python that lets you **call a method like it's a variable** — without using parentheses.
- It makes a **getter method** behave like an **attribute**.
- So you can **access data safely**, **like a variable**, while **hiding logic** behind the scenes.

### @classmethod
Some thing you want some function associated with class, not with the instances/class. It's not need self thing.
- To **track or manage shared state** across instances.
- To **encapsulate behaviour** that's related to the class rather than any one object.
- Can modify/access **class variables**, not instance variables.
- **Class methods cannot directly access or modify instance attributes or methods** because they don't receive the instance (`self`)—they only receive the class (`cls`).
@classmethod:
- First arg is `cls` (class itself)
- Can access/modify class state
- Often used as factory methods

### @staticmethod
A `@staticmethod` is a method inside a class that **does not access**:
- The instance (`self`)
- The class itself (`cls`)
It behaves just like a **regular function**, but it lives **inside the class namespace** for organisational purposes.

@staticmethod:
- No automatic arguments (like self or cls)
- Cannot access class or instance state
- Used for general utility/helper functions

- **Use `@classmethod`** when:
    - You need to **create or configure** class objects (`cls(...)`).
    - You need access to **class-level attributes** (`cls.species`, etc.).
    - You want the method to **work correctly in subclasses**.

- **Use `@staticmethod`** when:
    - The method is **logically related** to the class but **doesn’t need any class or instance context**.
    - For pure utility/helper methods.
### @abstractmethod

`@abstractmethod` is a **decorator** in Python used inside an **abstract class** to declare **methods that must be implemented** by any subclass.

### `del` keyword
It **decreases the reference count** of the object. When the count becomes 0, the memory is freed by Python’s garbage collector.
#### The `del` keyword is used to **delete**:

- a **variable**
- an **object**
- an **element from a list**
- an **attribute from an object**
#### When should I use `del`?

- To **manually free up memory** in long-running scripts.
- To **remove sensitive data** early (e.g., passwords).
- To **modify data structures** like lists or dicts.
- To **clean up attributes or objects** no longer needed.

Example
```
class Dog:
    def __init__(self):
        self.name = "Bruno"
        self.age = 5

dog = Dog()
print(dog.name)  # Bruno

del dog.name     # delete attribute
# print(dog.name)  # ❌ AttributeError
```
### Reference count(memory management in Python)

In Python, **everything is an object** (integers, strings, lists, functions, etc.).  
When you create an object, Python stores it in memory and keeps track of **how many variables (or other objects)** are pointing to it.

This number is called the **reference count**.
####  Example:

`a = [1, 2, 3] 
b = a 
c = a`

- List `[1, 2, 3]` is created once.
- `a`, `b`, and `c` all point to **the same list**.
-  The reference count is 3.
### <mark style="background: #FF5582A6;">Garbage Collection</mark>

Python uses a **garbage collector** to:
- Monitor reference counts.
- Automatically **free memory** when objects are no longer needed.
- Clean up circular references too (via **mark-and-sweep** algorithm).

### What does `__name__` mean?

In every Python file:

- Python automatically defines a built-in variable called `__name__`.
- If the file is **run directly**, `__name__` is set to `"__main__"`.
- If the file is **imported as a module** into another file, `__name__` is set to the module's name (i.e., the filename without `.py`).
- It checks **if the script is being run directly** and not being imported. If true, it runs the code inside the block.

Small Things to help scalable program:
1. `sys.exit()` immediately terminates the program. `sys.exit("msg")` prints the message and stops execution.
2. The `raise` keyword is used to **manually trigger an exception** in your program. To **create custom errors** instead of letting the program fail silently or behave incorrectly. To make your code **fail fast** when conditions are not met.
3. `raise` throws an exception; can be caught using `try-except`. `sys.exit()` stops the program immediately; exits Python interpreter.
4. 