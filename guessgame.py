print("NUMBER GUESSING GAME")
print("guess a number between 1 to 9")
guess=int(input("Enter your guess here:"))
if guess < 4:
    print(guess,"is a small guess. Guess a number higher than",guess)
elif guess > 8:
    print(guess,"is a correct guess.... Congraulations")