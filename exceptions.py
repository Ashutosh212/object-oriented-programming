# SyntaxError
# ValueError
# NameError
def get_int():
    while True:
        try: 
            x = int(input("Value of x? "))
        except ValueError:
            print("x is not an integer")
        else: # if no exception is going to happen, run this
            break
    return x

def main():
    x = get_int()  # yes, this is kinda abstraction
    print(f"x is {x}")

main()