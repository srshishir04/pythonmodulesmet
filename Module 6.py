#Task 1
import random
def roll_dice():
    return random.randint(1,6)
while True:
    dice_roll=roll_dice()
    print("Dice Roll Result: ",dice_roll)
    if dice_roll==6:
        break
print("You rolled a 6!Game over")

#Task 2
import random
def roll_of_dice(sides):
    return random.randint(1,sides)
try:
    sides=int(input("Enter the number of sides on the dice: "))
    if sides < 1:
        print("Invalid input. Number of sides must be at least 1.")
    else:
        while True:
            dice_of_roll=roll_of_dice(sides)
            print("Dice Roll Result:", dice_of_roll)
            if dice_of_roll==sides:
                print(f"Congratulations! You rolled the maximum number ({sides}). Game Over.")
                break
except ValueError:
    print("Invalid input. Please enter a valid number of sides.")

#Task 3
def gasoline(gas):
    liter=gas*3.7689
    return liter
while True:
    inp=float(input("Enter the volume of gallons: "))
    res=gasoline(inp)
    if inp<0:
        print("Invalid input")
        break
    else:
        print(res)

#Task 4
def function(x):
    num=0
    for i in x:
        num+=int(i)
    return num
print(function([1,2,3,4,5]))

#Task 5
def remove_odd_numbers(input_list):
    even_numbers=[num for num in input_list if num%2==0]
    return even_numbers

original_list=[1,2,3,4,5,6,7,8,9,10]
cut_out_list=remove_odd_numbers(original_list)
print("Original list: ",original_list)
print("Even numbers only: ",cut_out_list)

#Task 6
def function(diameter,price):
    radius=diameter/2
    area_square_meter= 3.1416 *(radius**2)/10000
    unit_price=price/area_square_meter
    return unit_price
diameter1=float(input("Enter the diameter of first pizza in (cm): "))
price1=float(input("Enter the price of first pizza in (euros): "))

diameter2=float(input("Enter the diameter of second pizza in (cm): "))
price2=float(input("Enter the price of second pizza in (euros): "))

unit_price1=function(diameter1,price1)
unit_price2=function(diameter2,price2)

if unit_price1<unit_price2:
    print("The first pizza provides better value for money")
elif unit_price2<unit_price1:
    print("The second pizza provides better value for money")
else:
    print("The both pizza have the same value")



