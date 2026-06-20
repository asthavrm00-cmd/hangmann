import random

easy_words = ["cat", "dog", "sun", "book", "fish","mind","kind","hand","ball","joke"]
medium_words = ["python", "laptop", "garden", "school", "friend","house","nightmare","phone","general","codealpha","google"]
hard_words = ["developer", "hangman", "computer", "algorithm", "internship","microsoft","acknowledgment","scientific"]

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("🎮 Welcome to Hangman Game!")

print("\nChoose Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    word = random.choice(easy_words)
elif choice == "2":
    word = random.choice(medium_words)
elif choice == "3":
    word = random.choice(hard_words)
else:
    print("Invalid choice! Defaulting to Easy.")
    word = random.choice(easy_words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

display = ["_" for _ in word]

while wrong_guesses < max_attempts and "_" in display:

    print(hangman_stages[wrong_guesses])
    print("\nWord:", " ".join(display))
    print("Guessed Letters:", ", ".join(guessed_letters))

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

print(hangman_stages[wrong_guesses])

if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)

play_again = input("\nDo you want to play again? (yes/no): ").lower()

if play_again == "yes":
    print("Restart the program to play again!")
else:
    print("Thanks for playing!")