students =[]
students.append(("Amir", (30,30,89,100)))
students.append(("Timo", (40,70,49,90)))
students.append(("Outi", (48,78,79,30)))

nametofind = input("Enter the name to search: ")
found = False
for students in students:
    if students[0] == nametofind:
        print(f"The name, {students[0]}")
        print(f"The grade,{students[1]}")
        found = True
    if not found:
        print("The student doesn't exist")

