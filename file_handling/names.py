# name = input("What's your name? ")

# file = open("file_handling/names.txt", "a") # replacing w with a to append
# file.write(f"{name}\n")  # it's recreating the file everytime by deleting all the previous concept
# file.close()

# inserting name
# with open("file_handling/names.txt", "a") as file:
    # file.write(f"{name}\n")

names = []
with open("file_handling/names.txt", "r") as file:
    # lines = file.readlines()


    for line in file:
        names.append(line.rstrip())
        # print("hello", line.rstrip()[0])
        
for name in sorted(names):
    print(f"Hello, {name}")