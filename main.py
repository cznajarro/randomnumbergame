import random
answer = random.randint(1,100)
tries = 5
while tries > 0:
    x = int(input("Guess a number 1- 100:"))
    if x == answer:
        print("You're right! You win!")
        break
    elif x > answer:
        print("Too high!")
        tries -= 1
    elif x < answer:
        print("Too low!")
        tries -= 1
if tries == 0:
    print("You lose!")
    print("The answer was " + str(answer) + ".")
#hello!