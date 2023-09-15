#Task1
name = input("What is your name? ")
print("Hello " + name + "!" )

#Task2
radius = float(input("Enter the radius: "))
pie = 3.1416
area = (pie * (radius**2))
print("The area of the circle is: " + str(area))

#Task3
Length = float(input("Enter the length of the rectangle: "))
Width = float(input("Enter the width of the rectangle: "))
perimeter = ((Length+Width)*2)
area = (Length*Width)
print("The perimeter of the rectangle is: " + str(perimeter))
print("The area of the rectangle is: " + str(area))

#Task4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
sum = (num1 + num2 + num3)
product = (num1 * num2 * num3)
average = sum/3
print("The sum of these number is: " + str(sum))
print("The product of these number is: " + str(product))
print("The average of these number is: " + str(average))

#Task5
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot= 13.3

talents = float(input("Enter a mass in talents: "))
pounds = float(input("Enter a mass in pounds: "))
lots = float(input("Enter a mass in lot: "))

total_kilograms = talents * pounds_per_talent + pounds
total_grams = total_kilograms * 1000 + lots * lots_per_pound * grams_per_lot

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"The mass is equivalent to {kilograms} kilograms and {grams} grams.")





