#Task1
size = float(input("Enter the length of a zander in cm: "))
limit = (42-size)

if (size >= 42):
    print("You can keep the zander.")

else:
    print(f"The caught fish was {limit} centimeters below than the size limit")
    print("Please release the fish back into the lake")

#Task2
print("Here is the list of a cabin class of a cruise ship:")
print("LUX,")
print("A,")
print("B,")
print("C,")

cabin_class =(input("Enter the cabin class: "))

if (cabin_class == "LUX"):
    print("Upper-deck cabin with a balcony.")
elif (cabin_class == "A"):
    print("Above the car deck, equipped with a window.")
elif (cabin_class == "B"):
    print("Windowless cabin above the car deck.")
elif (cabin_class == "C"):
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

#Task3
gender = (input("Enter the biological gender (male or female): "))
hemoglobin_value = float(input("Enter the hemoglobin value(g/l): "))

if gender == "female":
    if 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin is normal")
    elif hemoglobin_value < 117:
        print("Your hemoglobin is low")
    else:
        print("Your hemoglobin is high")

if gender == "male":
    if 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin is normal")
    elif hemoglobin_value < 134:
        print("Your hemoglobin is low")
    else:
        print("Your hemoglobin is high")

else:
    print("Invalid gender")

#Task4
year = int(input("Enter a year: "))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{year} is Leap year")

else:
    print(f"{year} is not leap year")

