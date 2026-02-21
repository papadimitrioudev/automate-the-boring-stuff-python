# Number Guessing Game - Chapter 02 Project
# Demonstrates flow control concepts: if/elif/else, while loops, break, continue

print('Number Guessing Game')
print('I am thinking of a number between 1 and 20.')

# Secret number (in a real game, this would be random, but we haven't learned that yet)
secret_number = 7
attempts = 0
max_attempts = 6

# Main game loop
while attempts < max_attempts:
    print('Take a guess.')
    guess = input()

    # Input validation - check if input is a number
    if not guess.isdigit():
        print('Please enter a valid number!')
        continue

    # Convert to integer
    guess = int(guess)
    attempts = attempts + 1

    # Check if guess is in valid range
    if guess < 1 or guess > 20:
        print('Please guess a number between 1 and 20.')
        attempts = attempts - 1  # Don't count invalid guesses
        continue

    # Check the guess
    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        # Correct guess - break out of loop
        break

# Game over - check if won or lost
if guess == secret_number:
    print('Good job! You guessed my number in ' + str(attempts) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number) + '.')

# Ask if player wants to play again
print('')
print('Do you want to play again? (yes/no)')
play_again = input()

if play_again == 'yes':
    print('Great! Run the program again to play.')
else:
    print('Thanks for playing!')