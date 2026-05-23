import random
secret = random.randint(1, 100)
attempts = 0
while True:
    try:
        num = int(input("Enter a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if num < 1 or num > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    attempts += 1
    if num < secret:
        print("Number is too low. Try again.")
    elif num > secret:
        print("Number is too high. Try again.")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {attempts} attempts.")
        break
