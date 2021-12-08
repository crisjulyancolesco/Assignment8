print("Between 0-100, can you guess what number that Im' thinking?")

import random
Number = random.randint(0,100) 
Guess = int(input("What's your guess? "))

while Guess > Number:
    print("Your guess is greater than what I'm thinking!")
    Guess = int(input("What's your guess? ")) 

while Guess < Number:
    print("Your guess is less than what I'm thinking!")
    Guess = int(input("What's your guess? "))
 
while Guess == Number:
    print("Well done, you guessed it right!")
    break            