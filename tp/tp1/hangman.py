# Hangman Game
from random_word import RandomWords
r = RandomWords()

# Return a single random word
# Word to guess
secret_word = r.get_random_word()
print(secret_word)

# Le nombre de chance est 6
chances = 6

mot_secret = "python"

# Letters guessed by the player
guessed_letters = []

# Displaying initial empty spaces for letters in the word
display = []
for letter in secret_word:
    display.append("_")

# Game loop
while chances > 0 and "_" in display:
    # Display current state of the word
    print(" ".join(display))
    
    # Prompting user for a letter guess
    guess = input("Guess a letter: ").lower()
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    
    # Add the guessed letter to the list
    guessed_letters.append(guess)
    
    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        print("Good guess!")
        # Update the display to reveal the guessed letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        # Decrease the number of chances
        chances -= 1
    
    # Display the hangman
    print("Chances left:", chances)
    if chances == 6:
        print("  _______  ")
        print(" |       | ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|_        ")
    elif chances == 5:
        print("  _______  ")
        print(" |       | ")
        print(" |       O ")
        print(" |         ")
        print(" |         ")
        print("_|_        ")
    elif chances == 4:
        print("  _______  ")
        print(" |       | ")
        print(" |       O ")
        print(" |       | ")
        print(" |         ")
        print("_|_        ")
    elif chances == 3:
        print("  _______  ")
        print(" |       | ")
        print(" |       O ")
        print(" |      /| ")
        print(" |         ")
        print("_|_        ")
    elif chances == 2:
        print("  _______  ")
        print(" |       | ")
        print(" |       O ")
        print(" |      /|\\")
        print(" |         ")
        print("_|_        ")
    elif chances == 1:
        print("  _______  ")
        print(" |       | ")
        print(" |       O ")
        print(" |      /|\\")
        print(" |      /  ")
        print("_|_        ")
    elif chances == 0:
        print("  _______  ")
        print(" |       | ")
        print(" |       O ")
        print(" |      /|\\")
        print(" |      / \\")
        print("_|_        ")
        print("Game over! The word was:", secret_word)

# Check if the player won or lost
if "_" not in display:
    print("Congratulations! You guessed the word:", secret_word)
