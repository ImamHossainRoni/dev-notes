import random

def getAnswer(number):
    if number == 1:
        print("It is certain")
    elif number == 2:
        print("It is unfinished")
    elif number == 3:
        print("It is finished")
    elif number == 4:
        print("Its number 4")
    elif number == 5:
        print("It is Number 5")
r = random.randint(1,6)
myvar = getAnswer(r)
print(myvar)