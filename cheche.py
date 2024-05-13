import random

# Generate a random number between 1 and 10
hidden_number = random.randint(1, 10)

# Number of chances
chances = 3

# Loop through the chances
for attempt in range(chances):
    # Get user's guess
    guess = int(input("Guess the number between 1 and 10: "))

    # Check if the guess is correct
    if guess == hidden_number:
        print("Congratulations! You guessed the correct number!")
        break
    else:
        # Provide a hint
        if guess < hidden_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

# Check if the user ran out of chances
else:
    print(f"Sorry, you've run out of chances. The hidden number was {hidden_number}.")
