import random

def computerGuess(x): 
    #use this function if you want to a guess from computer(e.g x=100, A number will build between 1 and 100)
    low = 1
    high = x
    guess = ''
    while guess != "c" and low != high:

        randomNumber = random.randint(low,high)
        guess = input(f"Is it {randomNumber}? high(h), low(l), correct(c), quit(q): ")

        if guess == "h":
            high = randomNumber - 1
        elif guess == "l":
            low = randomNumber + 1
        elif guess == "c":
            print(f"the number you chosen is {randomNumber}")
        elif guess == "q":
            break
        else:
            print("Please choose h,l or c")
    
              
def userGuess(x): #use this function if you want to make a guess yourself
    guess = 0
    random_number = random.randint(1,x)
   
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 0 and {x}, (-777 to quit): "))
            if guess == -777:
                break
            elif guess > random_number:
                print ("too high")
            elif guess < random_number:
                print("too low")
            elif guess == random_number:
                print (f"You have guessed the number: {guess}")
        except:
            print("Please guess a number")
