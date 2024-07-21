

import random
print("welcome to the number guessing game")
print("I am thinking of number between 1 to 100")
difficulty=input("choice difficulity type :Type easy or hard: ")
if difficulty =="easy":
    i=10
elif difficulty=="hard":
    i=5
else:
    print("write correct type")
    exit()
answer=random.randint(1,100)
print(f"you have {i} attemps for your guessing game")
counter=i
for b in range(i):
    counter-=1
    choice=int(input("your number "))
    if answer==choice:
        print(f"you guess right answer {answer}")
        break
    elif answer<choice:
        print("its high")
    elif answer>choice:
        print("its low")
    if counter==0 and difficulty!=choice:
        print("you lost the game lets restart the game")
    else :
        print("Guess again")
        print(f"you left with {counter} attemps")
