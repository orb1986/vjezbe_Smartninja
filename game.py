import random



secret = random.randint (1, 30)
print (secret)
guess = 0

#while guess != secret:
for x in range(2):
    print("Pokušaj: "+ str(x+1))
    guess = int(input("Guess the secret number (between 1 and 2): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        break
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))