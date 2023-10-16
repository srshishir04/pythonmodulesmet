#Task 1
import random

dice_number = int(input("Enter the amount of dice you want to roll: "))
sum = 0

for i in range(dice_number):
    roll=random.randint(1,6)
    print(f"Rolling a dice: {roll}")
    sum +=roll
print(f"Sum of all dice rolls {sum}")

#Task 2
numbers =[]
while True:
    user_input=input("Enter a number or press enter to quit: ")
    if user_input==(""):
        break
    else:
        user_input=float(user_input)
        numbers.append(user_input)
numbers.sort()
numbers.reverse()
print(numbers)

#Task 3


#Task 4
list=[]
for i in range(0,5):
    ask=input("Enter a city name: ")
    list.append(ask)
for n in list:
    print(n)










