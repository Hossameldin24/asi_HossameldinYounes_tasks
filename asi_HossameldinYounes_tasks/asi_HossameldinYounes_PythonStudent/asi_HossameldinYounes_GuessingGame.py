word = "hossam"
guessCount = 1


guess = input("Enter your guess: ")

if guess == word:
    print("You Win!")

while guess != word:
    if guessCount >= 3:
        print("You lose! ")
        break
    else:
        guess = input("Enter your guess: ")
        guessCount = guessCount + 1

if guess == word:
    print("You Win!")