import random

def computerGuess(x):
    low = 1
    high = x
    guess = ''
    while guess != "c" and low != high:
        randomNumber = random.randint(low,high)
        guess = input(f"Is it {randomNumber} ?, high(h), low(l), correct(c): ")
        if guess == "h":
            high = randomNumber - 1
        elif guess == "l":
            low = randomNumber + 1
            
        
    print(f"Tamin edilen sayı{randomNumber}")
        

def userGuess(x):
    guess = 0
    random_number = random.randint(1,x)
   
    while guess != random_number:
        guess = int(input(f"Guess a number between 0 and {x}: "))
        if guess > random_number:
            print ("too high")
        elif guess < random_number:
            print("too low")
         
    print (f"You have guessed the number: {guess}")

userGuess(10)


