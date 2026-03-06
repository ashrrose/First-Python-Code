
import random # This tool picks a random number

# 1. The computer picks a secret number between 1 and 10
secret_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10...")

# 2. We give the user 3 chances to guess
for attempt in range(3):
    guess = int(input("Take a guess: ")) # 'int' turns your text into a number

    if guess == secret_number:
        print("YOU GOT IT! 🏆 You're a natural! ")
        break # This stops the loop early because you won!
    elif guess < secret_number:
        print("Nope! Too low! Try again.")
    else:
        print("Too ambitious. Too high! Try again.")

# 3. If the loop finishes and you didn't 'break' out of it...
else:
    print("Game over! The number was " + str(secret_number) + ". Better luck next time!")