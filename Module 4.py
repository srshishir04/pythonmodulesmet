#Task1
number = 1
while number <=1000:
    if number % 3 == 0:
        print(number)
    number = number+1

#Task2
while True:
    inches =float(input("Enter a length in inches: "))
    if inches<0:
        print("Execution stopped.")
        break
    centimeters = inches * 2.54
    print(f"{inches}inches is equal to {centimeters}centimeters")

#Task3
# Initialize empty lists to store the numbers
numbers = []

# Prompt the user to enter numbers until they enter an empty string
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the input is an empty string
    if user_input == "":
        break

    try:
        # Try to convert the input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if any numbers were entered
if len(numbers) == 0:
    print("No numbers entered.")
else:
    # Find the smallest and largest numbers
    smallest = min(numbers)
    largest = max(numbers)

    # Print the results
    print("Smallest number:", smallest)
    print("Largest number:", largest)

#Task4
import random

target_number = random.randint(1,10)
gueses = 0

while True:
    user_guess = input("Guess the number between 1 and 10: ")
    try:
        user_guess = int(user_guess)
    except value_error:
        print("Invalid input. Please enter a valid number between 1 and 10.")
        continue
    gueses += 1

    if user_guess == target_number:
        print(f"Correct!You guessed the number {target_number} in {gueses} attempts")
        break

    elif user_guess < target_number:
        print("Too low.Try again.")

    else:
        print("Too high.Try again.")

#Task5
correct_username= "python"
correct_password= "rules"

attempt = 0

while attempt < 5:
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect username and password,Please try again")
        attempt += 1

if attempt == 5:
    print("Access denied.You've exceeded the maximum limit")








