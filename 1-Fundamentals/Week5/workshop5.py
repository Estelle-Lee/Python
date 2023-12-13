import random

# parameter: tries:integer, start:integer, stop:integer
def guess_random_number(tries,start,stop):
    ran_num=random.randint(start,stop)
    while tries>0:
        print("Number of tries left: ",tries)
        guess=input(f"Guess a number between {start} and {stop}: ")

        guess=int(guess)

        if guess<ran_num:
            print("Guess higher!")
        if guess>ran_num:
            print("Guess lower!")
        if guess==ran_num:
            print("You guessed the correct number!")
            break

        tries -=1
        if tries==0:
            print("You have failed to guess the number:",ran_num)


# parameter: tries:integer, start:integer, stop:integer
def guess_random_num_linear(tries,start,stop):
    ran_num=random.randint(start,stop)
    print("The number for the program to guess is:",ran_num)
    for comp_num in range(start,stop+1):
        print("Number of tries left:",tries)

        tries -= 1
        if comp_num==ran_num:
            print("The program has guessed the correct number!")
            return tries
        else:
            print("The program is guessing...",comp_num)

        if tries==0:
            print("The program has failed to guess the correct number.")
            return tries

def guess_random_num_binary(tries,start,stop):
    ran_num=random.randint(start,stop)
    print("Random number to find:",ran_num)

    lower_bound=start
    upper_bound=stop

    while tries>0:
        pivot=(lower_bound+upper_bound)//2
        tries -= 1
        if pivot==ran_num:
            print("Found it!",ran_num)
            return tries
        if pivot<ran_num:
            print("Guessing higher!")
            lower_bound=pivot+1
        if pivot>ran_num:
            print("Guessing lower!")
            upper_bound=pivot-1
        
    print("Your program failed to find the number")
    return 0
    
        
        


# guess_random_number(5,0,20)
# print("tries:",guess_random_num_linear(10,0,10))
# guess_random_num_linear(5,0,10)
guess_random_num_binary(5,0,100)