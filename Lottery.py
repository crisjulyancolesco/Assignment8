print("Let's play lottery!")
print("Input three numbers and let' see if it will match the 3 random winning numbers.")
print("If the three numbers you input matched the 3 random winning numbers, you won. ")

def TryAgain():
    Again = 'yes'
    while Again[0] == 'y':
        First = int(input("First Number: "))
        Second = int(input("Second Number: "))
        Third = int(input("Third Number: "))

        import random 
        Number1 = random.randint(0,9)
        print(f"Randon Number: {Number1}")
        Number2 = random.randint(0,9)
        print(f"Randon Number: {Number2}")
        Number3 = random.randint(0,9)
        print(f"Randon Number: {Number3}")

        if First == Number1 and Second == Number2 and Third == Number3:
            print("You Win!")
        else:
            if First == Number1 and Second == Number3 and Third == Number2:
                print("You Win!")
            else:
                if First == Number2 and Second == Number1 and Third == Number3:
                    print("You Win!")
                else:
                    if First == Number2 and Second == Number3 and Third == Number1:
                        print("You Win!")
                    else:
                        if First == Number3 and Second == Number1 and Third == Number2:
                            print("You Win!")
                        else:
                            if First == Number3 and Second == Number2 and Third == Number1:
                                print("You Win!")
                            else:
                                if First != Number1 and Second != Number2 and Third != Number3:
                                        print("You loss!")
                                else:
                                    if First != Number1 and Second != Number3 and Third != Number2:
                                        print("You loss!")
                                    else:
                                        if First != Number2 and Second != Number1 and Third != Number3:
                                            print("You loss!")
                                        else:
                                            if First != Number2 and Second != Number3 and Third != Number1:
                                                print("You loss!")
                                            else:
                                                if First != Number3 and Second != Number1 and Third != Number2:
                                                    print("You loss!")
                                                else:
                                                    if First != Number3 and Second != Number2 and Third != Number1:
                                                        print("You loss!")
    
        Again = input("Wanna try your luck again? (Type 'y' if yes and 'n' if no): ")
    return
Again = TryAgain()
