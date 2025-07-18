## `global`
- Reading a global variable is okay without `global` if a local variable is not defined.
- Modifying a global variable **requires** `global`.
- Otherwise, Python thinks you're working with a new local variable → `UnboundLocalError`

## docstring
A **docstring** is a special kind of string used to **document your code** — specifically functions, classes, and modules.

It helps:
- Developers understand **what your function/class/module does**
- Tools like VS Code, PyCharm, and `help()` to show useful info
- Auto-generate documentation (e.g., Sphinx, pdoc, etc.)

## command-line arguments
```
python main.py hello world
```

```
import sys
print(sys.argv)
# output: ['main.py', 'hello', 'world']
```
Python assumes **you might want those arguments**.

## argparse
- `argparse` is a standard module for command-line input.
- Use `type=int` or `type=str` to automatically convert inputs.
#### Step 1
```
parser = argparse.ArgumentParser()
```
- Creates an argument parser that understands command-line inputs like `-n 5`.
#### Step 2
```
parser.add_argument("-n", dest="count", type=int)
```
- `-n` → defines the flag
- `args.n` → access its value
#### Step 3
```
args = parser.parse_args()
```
- This **parses** the actual values from the command line

## \*args and  \*\*kwargs
\*args = arbitrary number of positional arguments (as a tuple)
\*\*kwargs = arbitrary number of keyword arguments (as a dict)

Use when:
- You don’t know how many inputs you'll get
- You want flexible interfaces
- You forward arguments to another function

```
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Ashu", "John", "Maria")
# Output:
# Hello, Ashu!
# Hello, John!
# Hello, Maria!
```
```
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} => {value}")

show_info(name="Ashu", age=25, city="Delhi")
# Output:
# name => Ashu
# age => 25
# city => Delhi
```

## map()
The `map()` function in Python is used to **apply a function** to **each item** of an iterable (like a list, tuple, etc.) and return a **map object** (which is iterable).
```
map(function, iterable)
```
- `function`: A function to apply to each element of the iterable.
- `iterable`: A sequence (like list, tuple, etc.) to apply the function to.

You can pass **more than one iterable** if the function takes more than one argument:
```
def add(a, b):
    return a + b

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

result = map(add, nums1, nums2)
print(list(result))  # [5, 7, 9]
```
## filter()
`filter()` is used to **filter elements** from an iterable based on a **function that returns True or False**.
```
filter(function, iterable)
```
- `function`: A function that returns `True` (keep the item) or `False` (discard it).
- `iterable`: A sequence (like list, tuple, etc.) to filter.
```
def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
result = filter(is_even, nums)
print(list(result))  # [2, 4, 6]
```

## `yield`
- `yield` is a special keyword in Python that turns a **function into a generator**.
- `yield` is like `return`, but instead of **ending the function**, it **pauses** it and saves its state.
- It lets you return **a value at a time**, and **resume** from where you left off next time.
```
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)

or

gen = count_up_to(3)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

or 

print(*count_up_to(3))  # 1 2 3

```