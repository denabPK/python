def add_student():
    with open("students.txt", "a") as file:
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        file.write(name + "," + marks + "\n")

def view_students():
    with open("students.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            print(f"Name: {name}, Marks: {marks}")

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
