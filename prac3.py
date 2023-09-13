student = {
    "name" : "Timo",
    "age" : 25,
    "grade": "A",
    "courses": ["Math","Physics","Programming"]
}

#Accessing dictionary values:
print("Name: ",student["name"])
print("age: ",student["age"])
print("grade: ",student["grade"])
print("courses: ",student["courses"])

student['age'] = 25
student['courses'].append("language")
student["city"] = "Espoo"

#Iterating through the dic.
for key, value in student.items():
    print(key + " :",value)

del student["grade"]
#checking if a key exists in the dictionary

if "age" in student:
    print("Age exist and here is the value: ", student["age"])
else:
    print("Age not found in the dictionary")