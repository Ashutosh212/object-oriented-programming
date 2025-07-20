students = []

with open("file_handling/names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # print(f"{name} from {house}")
        # students.append(f"{name} from {house}")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} from {student['house']}")