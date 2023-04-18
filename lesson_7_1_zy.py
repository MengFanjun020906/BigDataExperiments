import random

num = random.randint(1, 10)

while True:
    try:
        guess = int(input('Enter a number between 1 and 10: '))
    except Exception as e:
        print("Input error! Please enter a number between 1 and 10.")
        continue
    if guess > num:
        print("Too big:", guess)
    elif guess < num:
        print("Too small:", guess)
    else:
        print("Congratulations! You guessed it right!")
        break
